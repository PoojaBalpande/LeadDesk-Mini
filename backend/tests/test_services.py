import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.db.base import Base
from app.exceptions.repository import DuplicateEntityError, EntityNotFoundError
from app.exceptions.service import ValidationError
from app.models.enums import LeadSource, LeadStatus, UserRole
from app.repositories.lead_repository import LeadRepository
from app.repositories.user_repository import UserRepository
from app.schemas.lead import LeadCreate, LeadUpdate
from app.schemas.user import UserCreate, UserLogin
from app.services.auth_service import AuthService
from app.services.lead_service import LeadService
from app.services.user_service import UserService


@pytest.fixture
def db_session() -> Session:
    """Provide an in-memory database session for service layer tests."""
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    session_factory = sessionmaker(bind=engine)
    session = session_factory()
    try:
        yield session
    finally:
        session.close()


def test_user_service_logic(db_session: Session):
    """Test UserService business logic rules and error handling."""
    user_repo = UserRepository(db_session)
    user_service = UserService(user_repo)

    # 1. Create User
    user_create = UserCreate(
        name="Charlie Sales",
        email="charlie@leaddesk.com",
        password="securepassword123",
        role=UserRole.SALES,
    )
    user = user_service.create_user(user_create)
    assert user.id is not None
    assert user.email == "charlie@leaddesk.com"

    # 2. Duplicate Email Error
    with pytest.raises(DuplicateEntityError):
        user_service.create_user(user_create)

    # 3. Change Role
    updated = user_service.change_role(user.id, UserRole.MANAGER)
    assert updated.role == UserRole.MANAGER

    # 4. Get Profile
    profile = user_service.get_profile(user.id)
    assert profile.name == "Charlie Sales"

    # 5. Entity Not Found Error
    with pytest.raises(EntityNotFoundError):
        user_service.get_profile(99999)

    # 6. Validate Email
    assert user_service.validate_email("charlie@leaddesk.com") is False
    assert user_service.validate_email("newuser@leaddesk.com") is True


def test_lead_service_logic(db_session: Session):
    """Test LeadService business rules, assignment, and status transitions."""
    user_repo = UserRepository(db_session)
    lead_repo = LeadRepository(db_session)

    user_service = UserService(user_repo)
    lead_service = LeadService(lead_repo, user_repo)

    sales_user = user_service.create_user(
        UserCreate(name="Sales Rep 1", email="rep1@leaddesk.com", password="password123")
    )

    # 1. Create Lead with valid assigned user
    lead_create = LeadCreate(
        name="Delta Inc",
        email="hello@delta.com",
        phone="+15550001111",
        status=LeadStatus.NEW,
        source=LeadSource.WEBSITE,
        assigned_user_id=sales_user.id,
    )
    lead = lead_service.create_lead(lead_create)
    assert lead.id is not None
    assert lead.assigned_user_id == sales_user.id

    # 2. Create Lead with invalid assigned user -> EntityNotFoundError
    invalid_lead_create = LeadCreate(
        name="Bad Lead",
        email="bad@lead.com",
        assigned_user_id=999999,
    )
    with pytest.raises(EntityNotFoundError):
        lead_service.create_lead(invalid_lead_create)

    # 3. Change Status
    updated_lead = lead_service.change_status(lead.id, LeadStatus.QUALIFIED)
    assert updated_lead.status == LeadStatus.QUALIFIED

    # 4. Assign User
    reassigned = lead_service.assign_user(lead.id, None)
    assert reassigned.assigned_user_id is None

    # 5. Update Lead
    update = LeadUpdate(company="Delta Systems LLC")
    updated_company = lead_service.update_lead(lead.id, update)
    assert updated_company.company == "Delta Systems LLC"

    # 6. Search Leads empty query validation error
    with pytest.raises(ValidationError):
        lead_service.search_leads("   ")

    # 7. Validate duplicate lead check
    assert lead_service.validate_duplicate_lead("hello@delta.com") is False
    assert lead_service.validate_duplicate_lead("unique@delta.com") is True


def test_auth_service_placeholders(db_session: Session):
    """Test AuthService raising NotImplementedError placeholders for Phase 5."""
    user_repo = UserRepository(db_session)
    user_service = UserService(user_repo)
    auth_service = AuthService(user_service)

    user_create = UserCreate(name="Test User", email="test@example.com", password="password123")
    user_login = UserLogin(email="test@example.com", password="password123")

    with pytest.raises(NotImplementedError):
        auth_service.register(user_create)

    with pytest.raises(NotImplementedError):
        auth_service.login(user_login)

    with pytest.raises(NotImplementedError):
        auth_service.refresh_token("dummy_token")

    with pytest.raises(NotImplementedError):
        auth_service.logout("dummy_token")

    with pytest.raises(NotImplementedError):
        auth_service.current_user("dummy_token")

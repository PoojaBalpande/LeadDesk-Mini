pytest_plugins = []

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.db.base import Base
from app.models.enums import LeadSource, LeadStatus, UserRole
from app.models.lead import Lead
from app.models.user import User
from app.repositories.lead_repository import LeadRepository
from app.repositories.user_repository import UserRepository


@pytest.fixture
def db_session() -> Session:
    """Provide an isolated in-memory SQLite session for repository tests."""
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    session_factory = sessionmaker(bind=engine)
    session = session_factory()
    try:
        yield session
    finally:
        session.close()


def test_user_repository_crud_and_queries(db_session: Session):
    """Test all UserRepository methods."""
    user_repo = UserRepository(db_session)

    # 1. Create
    user = User(
        name="Alice Rep",
        email="alice@leaddesk.com",
        password_hash="pass_hash_1",
        role=UserRole.SALES,
    )
    created_user = user_repo.create(user)
    assert created_user.id is not None

    # 2. Get by ID & Email
    assert user_repo.get_by_id(created_user.id) == created_user
    assert user_repo.get_by_email("alice@leaddesk.com") == created_user
    assert user_repo.email_exists("alice@leaddesk.com") is True
    assert user_repo.email_exists("unknown@leaddesk.com") is False

    # 3. List
    users = user_repo.list_users()
    assert len(users) == 1

    # 4. Update
    created_user.name = "Alice Updated"
    updated_user = user_repo.update(created_user)
    assert updated_user.name == "Alice Updated"

    # 5. Delete
    deleted = user_repo.delete(updated_user)
    assert deleted is True
    assert user_repo.get_by_id(created_user.id) is None


def test_lead_repository_search_and_filters(db_session: Session):
    """Test LeadRepository filtering, searching, counting, and pagination."""
    user_repo = UserRepository(db_session)
    lead_repo = LeadRepository(db_session)

    user = user_repo.create(
        User(name="Bob Manager", email="bob@leaddesk.com", password_hash="hash", role=UserRole.MANAGER)
    )

    lead1 = lead_repo.create(
        Lead(
            name="Alpha Corp",
            email="info@alpha.com",
            company="Alpha Systems",
            status=LeadStatus.NEW,
            source=LeadSource.WEBSITE,
            assigned_user_id=user.id,
        )
    )

    lead2 = lead_repo.create(
        Lead(
            name="Beta Ltd",
            email="contact@beta.org",
            company="Beta Global",
            status=LeadStatus.WON,
            source=LeadSource.REFERRAL,
            assigned_user_id=None,
        )
    )

    # Filter by Status
    new_leads = lead_repo.filter_by_status(LeadStatus.NEW)
    assert len(new_leads) == 1
    assert new_leads[0].id == lead1.id

    # Filter by Source
    referrals = lead_repo.filter_by_source(LeadSource.REFERRAL)
    assert len(referrals) == 1
    assert referrals[0].id == lead2.id

    # Filter by Assigned User
    assigned_leads = lead_repo.filter_by_assigned_user(user.id)
    assert len(assigned_leads) == 1
    assert assigned_leads[0].id == lead1.id

    # Count by Status
    assert lead_repo.count_by_status(LeadStatus.NEW) == 1
    assert lead_repo.count_by_status(LeadStatus.LOST) == 0

    # Search
    search_res = lead_repo.search("Beta")
    assert len(search_res) == 1
    assert search_res[0].id == lead2.id

    # Recent leads
    recent = lead_repo.recent_leads(limit=5)
    assert len(recent) == 2

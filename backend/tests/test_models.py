import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.db.base import Base
from app.models.enums import LeadSource, LeadStatus, UserRole
from app.models.lead import Lead
from app.models.user import User


@pytest.fixture
def db_session() -> Session:
    """Fixture providing an in-memory SQLite database session for ORM testing."""
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    session_factory = sessionmaker(bind=engine)
    session = session_factory()
    try:
        yield session
    finally:
        session.close()


def test_user_model_creation(db_session: Session):
    """Test creating a User instance in the database."""
    user = User(
        name="Test Manager",
        email="manager@leaddesk.com",
        password_hash="hashed_password_123",
        role=UserRole.MANAGER,
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)

    assert user.id is not None
    assert user.name == "Test Manager"
    assert user.email == "manager@leaddesk.com"
    assert user.role == UserRole.MANAGER
    assert user.created_at is not None
    assert user.updated_at is not None


def test_lead_model_creation_and_relationship(db_session: Session):
    """Test creating a Lead instance with assigned User relationship."""
    user = User(
        name="Sales Rep",
        email="sales@leaddesk.com",
        password_hash="secret_hash",
        role=UserRole.SALES,
    )
    db_session.add(user)
    db_session.commit()

    lead = Lead(
        name="Enterprise Client",
        email="contact@enterprise.com",
        phone="+15551234567",
        company="Enterprise Inc",
        message="Demanding enterprise demo",
        status=LeadStatus.QUALIFIED,
        source=LeadSource.WEBSITE,
        assigned_user_id=user.id,
    )
    db_session.add(lead)
    db_session.commit()
    db_session.refresh(lead)

    assert lead.id is not None
    assert lead.status == LeadStatus.QUALIFIED
    assert lead.source == LeadSource.WEBSITE
    assert lead.assigned_user_id == user.id
    assert lead.assigned_user.email == "sales@leaddesk.com"
    assert len(user.leads) == 1
    assert user.leads[0].name == "Enterprise Client"


def test_enum_defaults(db_session: Session):
    """Test default Enum values for User and Lead models."""
    user = User(
        name="Default User",
        email="default@leaddesk.com",
        password_hash="hash",
    )
    lead = Lead(
        name="Default Lead",
        email="lead@example.com",
    )
    db_session.add_all([user, lead])
    db_session.commit()

    assert user.role == UserRole.SALES
    assert lead.status == LeadStatus.NEW
    assert lead.source == LeadSource.OTHER

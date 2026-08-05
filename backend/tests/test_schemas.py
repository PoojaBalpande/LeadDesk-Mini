from datetime import datetime, timezone

import pytest
from pydantic import ValidationError

from app.models.enums import LeadSource, LeadStatus, UserRole
from app.schemas.lead import LeadCreate, LeadResponse, LeadUpdate
from app.schemas.user import UserCreate, UserLogin, UserResponse


def test_user_create_schema():
    """Test valid UserCreate schema validation."""
    data = {
        "name": "Jane Admin",
        "email": "admin@leaddesk.com",
        "password": "securepassword123",
        "role": UserRole.ADMIN,
    }
    schema = UserCreate(**data)
    assert schema.name == "Jane Admin"
    assert schema.email == "admin@leaddesk.com"
    assert schema.role == UserRole.ADMIN


def test_user_create_invalid_email():
    """Test UserCreate invalid email failure."""
    with pytest.raises(ValidationError):
        UserCreate(name="Bad Email", email="not-an-email", password="validpassword123")


def test_user_create_short_password():
    """Test UserCreate short password validation failure."""
    with pytest.raises(ValidationError):
        UserCreate(name="Short Pass", email="user@example.com", password="123")


def test_user_login_schema():
    """Test UserLogin schema validation."""
    login = UserLogin(email="user@example.com", password="secretpassword")
    assert login.email == "user@example.com"
    assert login.password == "secretpassword"


def test_user_response_from_attributes():
    """Test UserResponse ORM attribute binding and password exclusion."""
    class DummyUserORM:
        id = 1
        name = "Jane Admin"
        email = "admin@leaddesk.com"
        role = UserRole.ADMIN
        password_hash = "secret_hash_not_exposed"
        created_at = datetime.now(timezone.utc)
        updated_at = datetime.now(timezone.utc)

    orm_obj = DummyUserORM()
    response = UserResponse.model_validate(orm_obj)
    assert response.id == 1
    assert response.name == "Jane Admin"
    assert response.email == "admin@leaddesk.com"
    assert response.role == UserRole.ADMIN
    assert not hasattr(response, "password_hash")


def test_lead_create_schema():
    """Test valid LeadCreate schema validation."""
    data = {
        "name": "Acme Lead",
        "email": "info@acme.com",
        "phone": "+15551234567",
        "company": "Acme Inc",
        "message": "Interested in sales demo.",
        "status": LeadStatus.NEW,
        "source": LeadSource.WEBSITE,
    }
    lead = LeadCreate(**data)
    assert lead.name == "Acme Lead"
    assert lead.email == "info@acme.com"
    assert lead.status == LeadStatus.NEW


def test_lead_update_schema():
    """Test partial LeadUpdate schema validation."""
    update = LeadUpdate(status=LeadStatus.WON, company="Acme Global")
    assert update.status == LeadStatus.WON
    assert update.company == "Acme Global"
    assert update.name is None


def test_lead_response_from_attributes():
    """Test LeadResponse ORM attribute conversion."""
    now = datetime.now(timezone.utc)

    class DummyLeadORM:
        id = 42
        name = "Lead Fourty Two"
        email = "lead42@example.com"
        phone = "+19876543210"
        company = "FortyTwo Corp"
        message = "Hello world"
        status = LeadStatus.QUALIFIED
        source = LeadSource.REFERRAL
        assigned_user_id = 7
        created_at = now
        updated_at = now

    lead_response = LeadResponse.model_validate(DummyLeadORM())
    assert lead_response.id == 42
    assert lead_response.assigned_user_id == 7
    assert lead_response.status == LeadStatus.QUALIFIED
    assert lead_response.source == LeadSource.REFERRAL

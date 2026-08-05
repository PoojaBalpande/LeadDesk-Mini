from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field

from app.models.enums import LeadSource, LeadStatus

# Flexible phone validation pattern allowing optional leading '+' and digits/spaces/dashes/parentheses (7-20 chars)
PHONE_PATTERN = r"^\+?[0-9\s\-\(\)\.]{7,20}$"


class LeadCreate(BaseModel):
    """Schema for lead creation requests."""
    name: str = Field(..., min_length=1, max_length=100, examples=["Jane Smith"])
    email: EmailStr = Field(..., examples=["jane.smith@example.com"])
    phone: str | None = Field(
        default=None,
        max_length=20,
        pattern=PHONE_PATTERN,
        examples=["+15551234567"],
    )
    company: str | None = Field(default=None, max_length=100, examples=["Acme Corp"])
    message: str | None = Field(default=None, max_length=2000, examples=["Interested in enterprise plan."])
    status: LeadStatus = Field(default=LeadStatus.NEW)
    source: LeadSource = Field(default=LeadSource.OTHER)
    assigned_user_id: int | None = Field(default=None, description="ID of the assigned user.")


class LeadUpdate(BaseModel):
    """Schema for updating an existing lead (partial updates supported)."""
    name: str | None = Field(default=None, min_length=1, max_length=100)
    email: EmailStr | None = Field(default=None)
    phone: str | None = Field(default=None, max_length=20, pattern=PHONE_PATTERN)
    company: str | None = Field(default=None, max_length=100)
    message: str | None = Field(default=None, max_length=2000)
    status: LeadStatus | None = Field(default=None)
    source: LeadSource | None = Field(default=None)
    assigned_user_id: int | None = Field(default=None)


class LeadResponse(BaseModel):
    """Schema for lead public data returned in API responses."""
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    email: EmailStr
    phone: str | None
    company: str | None
    message: str | None
    status: LeadStatus
    source: LeadSource
    assigned_user_id: int | None
    created_at: datetime
    updated_at: datetime

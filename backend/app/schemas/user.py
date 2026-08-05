from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field

from app.models.enums import UserRole


class UserCreate(BaseModel):
    """Schema for user creation / registration requests."""
    name: str = Field(..., min_length=1, max_length=100, examples=["John Doe"])
    email: EmailStr = Field(..., examples=["john.doe@example.com"])
    password: str = Field(
        ...,
        min_length=8,
        max_length=128,
        description="Password must be between 8 and 128 characters.",
    )
    role: UserRole = Field(default=UserRole.SALES, description="Role assigned to the user.")


class UserLogin(BaseModel):
    """Schema for user authentication requests."""
    email: EmailStr = Field(..., examples=["john.doe@example.com"])
    password: str = Field(..., min_length=1, description="User password.")


class UserResponse(BaseModel):
    """Schema for user public data returned in API responses."""
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    email: EmailStr
    role: UserRole
    created_at: datetime
    updated_at: datetime

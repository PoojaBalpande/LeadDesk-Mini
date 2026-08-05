from typing import Any

from app.exceptions.repository import DuplicateEntityError, EntityNotFoundError
from app.models.enums import UserRole
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate


class UserService:
    """Service executing domain logic and business rule orchestration for users."""

    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def create_user(self, user_create: UserCreate) -> User:
        """Register a new user after verifying unique email constraints."""
        if self.user_repository.email_exists(user_create.email):
            raise DuplicateEntityError("User", "email", user_create.email)

        user = User(
            name=user_create.name,
            email=user_create.email,
            password_hash=user_create.password,  # Password hashing added in Phase 5
            role=user_create.role,
        )
        return self.user_repository.create(user)

    def update_user(self, user_id: int, user_data: dict[str, Any]) -> User:
        """Update existing user properties."""
        user = self.user_repository.get_by_id(user_id)
        if not user:
            raise EntityNotFoundError("User", user_id)

        if "email" in user_data and user_data["email"] != user.email and self.user_repository.email_exists(user_data["email"]):
            raise DuplicateEntityError("User", "email", user_data["email"])

        for field, value in user_data.items():
            if hasattr(user, field) and field not in ("id", "created_at", "updated_at"):
                setattr(user, field, value)

        return self.user_repository.update(user)

    def change_role(self, user_id: int, new_role: UserRole) -> User:
        """Update the assigned system role of a target user."""
        user = self.user_repository.get_by_id(user_id)
        if not user:
            raise EntityNotFoundError("User", user_id)

        user.role = new_role
        return self.user_repository.update(user)

    def get_profile(self, user_id: int) -> User:
        """Retrieve user profile by primary key ID."""
        user = self.user_repository.get_by_id(user_id)
        if not user:
            raise EntityNotFoundError("User", user_id)
        return user

    def validate_email(self, email: str) -> bool:
        """Verify whether an email is available for registration (True if available)."""
        return not self.user_repository.email_exists(email)

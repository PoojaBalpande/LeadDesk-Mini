from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User


class UserRepository:
    """Repository handling database persistence operations for the User entity."""

    def __init__(self, db: Session) -> None:
        self.db = db

    def get_by_id(self, user_id: int) -> User | None:
        """Fetch a User by primary key ID."""
        return self.db.get(User, user_id)

    def get_by_email(self, email: str) -> User | None:
        """Fetch a User by unique email address."""
        stmt = select(User).where(User.email == email)
        return self.db.scalars(stmt).first()

    def email_exists(self, email: str) -> bool:
        """Check if a User record with the given email exists."""
        return self.get_by_email(email) is not None

    def create(self, user: User) -> User:
        """Persist a new User entity in the database."""
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def update(self, user: User) -> User:
        """Update an existing User entity in the database."""
        self.db.commit()
        self.db.refresh(user)
        return user

    def delete(self, user: User) -> bool:
        """Remove a User entity from the database."""
        self.db.delete(user)
        self.db.commit()
        return True

    def list_users(self, skip: int = 0, limit: int = 100) -> list[User]:
        """Retrieve a paginated list of users."""
        stmt = select(User).offset(skip).limit(limit)
        return list(self.db.scalars(stmt).all())

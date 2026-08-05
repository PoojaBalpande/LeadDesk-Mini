from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.repositories.lead_repository import LeadRepository
from app.repositories.user_repository import UserRepository
from app.services.auth_service import AuthService
from app.services.lead_service import LeadService
from app.services.user_service import UserService


def get_user_repository(db: Session = Depends(get_db)) -> UserRepository:
    """Dependency provider for UserRepository."""
    return UserRepository(db)


def get_lead_repository(db: Session = Depends(get_db)) -> LeadRepository:
    """Dependency provider for LeadRepository."""
    return LeadRepository(db)


def get_user_service(user_repo: UserRepository = Depends(get_user_repository)) -> UserService:
    """Dependency provider for UserService."""
    return UserService(user_repository=user_repo)


def get_lead_service(
    lead_repo: LeadRepository = Depends(get_lead_repository),
    user_repo: UserRepository = Depends(get_user_repository),
) -> LeadService:
    """Dependency provider for LeadService."""
    return LeadService(lead_repository=lead_repo, user_repository=user_repo)


def get_auth_service(user_service: UserService = Depends(get_user_service)) -> AuthService:
    """Dependency provider for AuthService."""
    return AuthService(user_service=user_service)

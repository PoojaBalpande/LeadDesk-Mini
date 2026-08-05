from app.models.user import User
from app.schemas.user import UserCreate, UserLogin
from app.services.user_service import UserService


class AuthService:
    """Service handling authentication, JWT tokens, and session management.
    
    Note: Full implementation will be added in Phase 5.
    """

    def __init__(self, user_service: UserService) -> None:
        self.user_service = user_service

    def register(self, user_create: UserCreate) -> User:
        """Register a new user account."""
        raise NotImplementedError("Authentication will be implemented in Phase 5.")

    def login(self, credentials: UserLogin) -> dict[str, str]:
        """Authenticate user credentials and issue access tokens."""
        raise NotImplementedError("Authentication will be implemented in Phase 5.")

    def refresh_token(self, token: str) -> dict[str, str]:
        """Refresh an expired access token using a valid refresh token."""
        raise NotImplementedError("Authentication will be implemented in Phase 5.")

    def logout(self, token: str) -> bool:
        """Revoke a user session or access token."""
        raise NotImplementedError("Authentication will be implemented in Phase 5.")

    def current_user(self, token: str) -> User:
        """Resolve the currently authenticated User from a token string."""
        raise NotImplementedError("Authentication will be implemented in Phase 5.")

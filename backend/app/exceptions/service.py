from app.exceptions.base import ApplicationError


class ServiceError(ApplicationError):
    """Base exception for service and business logic operations."""


class ValidationError(ServiceError):
    """Raised when domain business rules or input validation fails."""


class AuthenticationError(ServiceError):
    """Raised when authentication credentials or tokens are invalid."""


class AuthorizationError(ServiceError):
    """Raised when a user lacks sufficient permissions for an action."""

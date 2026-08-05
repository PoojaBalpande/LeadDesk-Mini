from datetime import timedelta
from typing import Any


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Placeholder utility to verify a plain text password against a hashed password.

    Will be fully implemented in future Authentication phase (Phase 4.2+).
    """
    raise NotImplementedError("Password verification utility will be implemented in future phase.")


def get_password_hash(password: str) -> str:
    """Placeholder utility to generate a secure password hash.

    Will be fully implemented in future Authentication phase (Phase 4.2+).
    """
    raise NotImplementedError("Password hashing utility will be implemented in future phase.")


def create_access_token(
    subject: str | Any,
    expires_delta: timedelta | None = None,
) -> str:
    """Placeholder utility to encode a JWT access token for a given subject.

    Will be fully implemented in future Authentication phase (Phase 4.2+).
    """
    raise NotImplementedError("JWT creation utility will be implemented in future phase.")


def decode_access_token(token: str) -> dict[str, Any]:
    """Placeholder utility to decode and validate a JWT access token.

    Will be fully implemented in future Authentication phase (Phase 4.2+).
    """
    raise NotImplementedError("JWT verification utility will be implemented in future phase.")

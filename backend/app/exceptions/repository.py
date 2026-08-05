from app.exceptions.base import ApplicationError


class RepositoryError(ApplicationError):
    """Base exception for database and persistence operations."""


class EntityNotFoundError(RepositoryError):
    """Raised when a requested entity is not found in the database."""
    def __init__(self, entity_name: str, entity_id: str | int) -> None:
        self.entity_name = entity_name
        self.entity_id = entity_id
        super().__init__(f"{entity_name} with identifier '{entity_id}' was not found.")


class DuplicateEntityError(RepositoryError):
    """Raised when an operation violates a unique database constraint."""
    def __init__(self, entity_name: str, field_name: str, field_value: str) -> None:
        self.entity_name = entity_name
        self.field_name = field_name
        self.field_value = field_value
        super().__init__(f"{entity_name} with {field_name} '{field_value}' already exists.")

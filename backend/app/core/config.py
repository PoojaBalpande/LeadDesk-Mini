import json
from functools import lru_cache

from pydantic import field_validator, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application Settings Schema using Pydantic Settings."""

    # Project Information
    PROJECT_NAME: str = "LeadDesk Mini API"
    VERSION: str = "1.0.0"
    DEBUG: bool = False
    ENVIRONMENT: str = "development"
    API_V1_STR: str = "/api/v1"

    # Server Host & Port
    SERVER_HOST: str = "0.0.0.0"
    SERVER_PORT: int = 8000

    # Database Configuration
    DATABASE_URL: str = "sqlite:///./leaddesk.db"

    # Security & JWT Configuration
    SECRET_KEY: str = "dev-secret-key-change-in-production-min-32-chars-long!"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # CORS Allowed Origins
    BACKEND_CORS_ORIGINS: list[str] = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ]

    @field_validator("BACKEND_CORS_ORIGINS", mode="before")
    @classmethod
    def assemble_cors_origins(cls, v: str | list[str]) -> list[str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",") if i.strip()]
        elif isinstance(v, str) and v.startswith("["):
            try:
                return json.loads(v)
            except Exception:
                pass
        return v  # type: ignore

    @model_validator(mode="after")
    def validate_production_settings(self) -> "Settings":
        """Validate critical settings in production environment."""
        if self.ENVIRONMENT.lower() == "production":
            if "dev-secret-key" in self.SECRET_KEY:
                raise ValueError("SECRET_KEY must be securely configured for production environment.")
            if self.DEBUG:
                raise ValueError("DEBUG mode must be disabled in production environment.")
        return self

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    """Return cached Settings instance."""
    return Settings()


# Exposed settings singleton for easy import across modules
settings: Settings = get_settings()

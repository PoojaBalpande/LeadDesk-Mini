from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.core.config import settings
from app.core.logging import logger

# Configure engine connect arguments (e.g. SQLite thread check)
connect_args = {}
if settings.DATABASE_URL.startswith("sqlite"):
    connect_args["check_same_thread"] = False

# Create SQLAlchemy 2.x Engine
engine = create_engine(
    settings.DATABASE_URL,
    connect_args=connect_args,
    pool_pre_ping=True,  # Test connections before using them to handle dropped connections gracefully
    echo=settings.DEBUG,  # Log SQL statements in debug mode
)

# Configured Session factory for database sessions
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    expire_on_commit=False,
)


def get_db() -> Generator[Session, None, None]:
    """Dependency for acquiring database session with automatic lifecycle management."""
    db: Session = SessionLocal()
    try:
        yield db
    except Exception as exc:
        logger.error(f"Database session exception encountered: {exc}")
        db.rollback()
        raise
    finally:
        db.close()

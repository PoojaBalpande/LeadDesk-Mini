import logging
import sys

from app.core.config import settings


class CustomFormatter(logging.Formatter):
    """Custom formatter with standardized format for enterprise logging."""

    FORMAT = "%(asctime)s | %(levelname)-8s | %(name)s | %(filename)s:%(lineno)d | %(message)s"

    def __init__(self) -> None:
        super().__init__(fmt=self.FORMAT, datefmt="%Y-%m-%d %H:%M:%S")


def setup_logging(log_level: str | None = None) -> logging.Logger:
    """Configure centralized Python logging handler and formatter."""
    level_str = log_level or ("DEBUG" if settings.DEBUG else "INFO")
    level = getattr(logging, level_str.upper(), logging.INFO)

    root_logger = logging.getLogger()
    root_logger.setLevel(level)

    # Remove existing default handlers to avoid duplicate logs
    if root_logger.hasHandlers():
        root_logger.handlers.clear()

    # Create console stream handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)
    console_handler.setFormatter(CustomFormatter())

    root_logger.addHandler(console_handler)

    # Suppress verbose third-party loggers if not in DEBUG mode
    if not settings.DEBUG:
        logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
        logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)

    logger = logging.getLogger("leaddesk")
    logger.setLevel(level)
    return logger


# Instantiate reusable logger for the application
logger: logging.Logger = setup_logging()

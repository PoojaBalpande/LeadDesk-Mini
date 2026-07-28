from fastapi import APIRouter, Depends, status
from pydantic import BaseModel
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.logging import logger
from app.db.database import get_db

router = APIRouter()


class HealthResponse(BaseModel):
    status: str
    project: str
    version: str
    database_status: str


@router.get("/health", response_model=HealthResponse, status_code=status.HTTP_200_OK, tags=["Health"])
def health_check(db: Session = Depends(get_db)) -> HealthResponse:
    """Check health status of API service and database connectivity safely."""
    db_status = "disconnected"
    overall_status = "healthy"

    try:
        # Execute quick ping to verify database connectivity
        db.execute(text("SELECT 1"))
        db_status = "connected"
    except Exception as exc:
        logger.error(f"Health check database ping failed: {exc}")
        db_status = "disconnected"
        overall_status = "degraded"

    return HealthResponse(
        status=overall_status,
        project=settings.PROJECT_NAME,
        version=settings.VERSION,
        database_status=db_status,
    )

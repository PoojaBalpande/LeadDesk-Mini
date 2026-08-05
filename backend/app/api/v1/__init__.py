from fastapi import APIRouter

from app.api.v1.health import router as health_router

api_v1_router = APIRouter()

# Include v1 feature routers
api_v1_router.include_router(health_router)

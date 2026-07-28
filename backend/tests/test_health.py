from fastapi.testclient import TestClient

from app.core.config import get_settings
from app.main import app, create_application


def test_health_endpoint():
    """Test GET /api/v1/health endpoint response structure and database connectivity status."""
    client = TestClient(app)
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert "project" in data
    assert "version" in data
    assert "database_status" in data
    assert data["status"] == "healthy"
    assert data["database_status"] == "connected"


def test_app_factory():
    """Test Application Factory instantiation."""
    test_app = create_application()
    assert test_app.title == "LeadDesk Mini API"
    assert test_app.version == "1.0.0"


def test_settings_lru_cache():
    """Test configuration setting retrieval and caching."""
    s1 = get_settings()
    s2 = get_settings()
    assert s1 is s2

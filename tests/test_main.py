"""Unit tests for the Flask application."""
import pytest
from app.main import app


@pytest.fixture
def client():
    """Create test client."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_endpoint(client):
    """Test home endpoint returns correct data."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "healthy"
    assert "message" in data
    assert "version" in data


def test_health_endpoint(client):
    """Test health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "healthy"
    assert data["service"] == "secure-cicd-pipeline"


def test_info_endpoint(client):
    """Test info endpoint returns application details."""
    response = client.get("/api/info")
    assert response.status_code == 200
    data = response.get_json()
    assert "application" in data
    assert "features" in data
    assert isinstance(data["features"], list)
    assert len(data["features"]) > 0


def test_invalid_endpoint(client):
    """Test invalid endpoint returns 404."""
    response = client.get("/invalid-endpoint")
    assert response.status_code == 404

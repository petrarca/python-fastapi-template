"""Tests for the FastAPI application."""

from fastapi.testclient import TestClient

from src.app.app import app

client = TestClient(app)


def test_read_health():
    """Test the health endpoint returns the expected response."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_read_home():
    """Test the home endpoint returns a successful response."""
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]

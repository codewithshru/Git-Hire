"""Sanity tests for the application scaffold."""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_endpoint() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_readiness_endpoint() -> None:
    response = client.get("/health/ready")
    assert response.status_code == 200


def test_openapi_available() -> None:
    response = client.get("/api/v1/openapi.json")
    assert response.status_code == 200

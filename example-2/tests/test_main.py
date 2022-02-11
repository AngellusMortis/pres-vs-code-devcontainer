from unittest.mock import AsyncMock, patch

from fastapi.testclient import TestClient
import pytest

from main import app


@pytest.fixture(name="client")
def client_fixture() -> TestClient:
    return TestClient(app)


@patch("main.redis")
def test_root(redis, client: TestClient) -> None:
    redis.client.incr = AsyncMock(return_value=1)

    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Good News Everyone!", "count": 1}


def test_healthcheck(client: TestClient) -> None:
    response = client.get("/healthcheck/")
    assert response.status_code == 200

"""Integration tests for API endpoints."""

import pytest
from httpx import AsyncClient

pytestmark = pytest.mark.asyncio


@pytest.mark.asyncio
async def test_health_check(async_client: AsyncClient) -> None:
    """Test health check endpoint."""
    response = await async_client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


async def test_send_template_success(async_client: AsyncClient) -> None:
    """Test successful template message sending."""
    template_data = {
        "recipient": "1234567890",
        "template_name": "hello_world",
        "language_code": "en",
    }

    response = await async_client.post("/message/template", json=template_data)
    assert response.status_code == 202
    assert "status" in response.json()


async def test_send_template_validation(async_client: AsyncClient) -> None:
    """Test template message input validation."""
    invalid_data = {
        "recipient": "invalid",  # Should be numbers only
        "template_name": "",  # Should not be empty
        "language_code": "eng",  # Should be 2 chars
    }

    response = await async_client.post("/message/template", json=invalid_data)
    assert response.status_code == 422  # Validation error

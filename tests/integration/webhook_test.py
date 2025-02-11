"""Integration tests for WhatsApp message endpoints."""

import pytest
from httpx import AsyncClient

from tests.fixtures import whatsapp_media_message_fixture, whatsapp_text_message_fixture


@pytest.mark.asyncio
async def test_webhook_verification(async_client: AsyncClient) -> None:
    """Test WhatsApp webhook verification endpoint."""
    params = {
        "hub.mode": "subscribe",
        "hub.verify_token": "test_token",
        "hub.challenge": "challenge_code",
    }
    response = await async_client.get("/webhook", params=params)
    assert response.status_code == 200
    assert response.text == "challenge_code"


@pytest.mark.asyncio
async def test_webhook_text_message(async_client: AsyncClient) -> None:
    """Test receiving a text message through webhook."""
    payload = whatsapp_text_message_fixture()
    response = await async_client.post("/webhook", json=payload)
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_webhook_media_message(async_client: AsyncClient) -> None:
    """Test receiving a media message through webhook."""
    payload = whatsapp_media_message_fixture()
    response = await async_client.post("/webhook", json=payload)
    assert response.status_code == 200

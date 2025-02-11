"""Test configuration and common fixtures."""

import asyncio
from collections.abc import AsyncGenerator, Generator

import pytest
from fastapi import FastAPI
from httpx import AsyncClient

from backend.main import app


@pytest.fixture(scope="session")
def event_loop() -> Generator[asyncio.AbstractEventLoop, None, None]:
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
def app_instance() -> FastAPI:
    """Get FastAPI application."""
    return app


@pytest.fixture
async def async_client(app_instance: FastAPI) -> AsyncGenerator[AsyncClient, None]:
    """Create async client for testing."""
    async with AsyncClient(app=app_instance, base_url="http://test") as client:
        yield client

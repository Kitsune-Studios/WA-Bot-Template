"""Main module for FastAPI app."""

from contextlib import asynccontextmanager
from datetime import UTC, datetime
from os import getenv
from typing import Annotated

import ngrok
from fastapi import Depends, FastAPI, status
from fastapi.routing import APIRouter
from mangum import Mangum

from backend.middleware.custom_middleware import CustomMiddleware
from backend.routers.messages import messages

NGROK_AUTH_TOKEN = getenv("NGROK_AUTH_TOKEN")
NGROK_DOMAIN = getenv("NGROK_DOMAIN")


@asynccontextmanager
async def lifespan() -> ngrok.NgrokTunnel:
    """Start and stop ngrok tunnel."""
    ngrok.set_auth_token(NGROK_AUTH_TOKEN)
    ngrok.forward(
        addr=getenv("PORT_NUMBER", "8000"),
        domain=NGROK_DOMAIN,
    )
    yield
    ngrok.disconnect()


app = FastAPI(lifespan=lifespan)
app.add_middleware(CustomMiddleware)
handler = Mangum(app)
NOW = datetime.now(tz=UTC)


@app.get("/", status_code=status.HTTP_200_OK, tags=["App Info"])
def get_app_info() -> dict[str, str]:
    """Print info on app."""
    return {"info": "WhatsApp Bot", "app_version": "0.0.1"}


app.include_router(messages.router, tags=["Messages"])


# Dependency Injection Example
def get_current_user() -> str:
    """Return the current user."""
    return "current_user"


@app.get("/users/me", tags=["Users"])
def read_users_me(
    current_user: Annotated[str, Depends(get_current_user)],
) -> dict[str, str]:
    """Retrieve the current user."""
    return {"user": current_user}


# API Versioning
v1_router = APIRouter()


@v1_router.get("/items", tags=["v1"])
def read_items_v1() -> dict[str, list[str]]:
    """Retrieve items for version 1 of the API."""
    return {"items": ["item1", "item2"]}


@app.get("/items/{item_id}", tags=["v1"])
def read_item(item_id: int) -> dict[str, str]:
    """Retrieve a specific item by its ID."""
    return {"item_id": item_id, "item_name": f"item{item_id}"}


app.include_router(v1_router, prefix="/v1")

# OpenAPI Customization
app.title = "WA-Bot-Template API"
app.description = "API documentation for the WA-Bot-Template project"
app.version = "1.0.0"
app.contact = {
    "name": "Carlos Ferreyra",
    "url": "https://github.com/carlosferreyra",
    "email": "carlos@example.com",
}

"""Main module for FastAPI app."""

from contextlib import asynccontextmanager
from datetime import datetime
from os import getenv

import ngrok
from fastapi import FastAPI, status
from mangum import Mangum

from backend.routers.messages import messages


@asynccontextmanager
async def lifespan():
    """Start and stop ngrok tunnel."""
    assert getenv("NGROK_AUTH_TOKEN"), "NGROK_AUTH_TOKEN not set"
    assert getenv("PORT_NUMBER"), "PORT_NUMBER not set"
    assert getenv("NGROK_DOMAIN"), "NGROK_DOMAIN not set"
    ngrok.set_auth_token(getenv("NGROK_AUTH_TOKEN"))
    ngrok.forward(
        addr=getenv("PORT_NUMBER", "8000"),
        domain=getenv("NGROK_DOMAIN"),
    )
    yield
    ngrok.disconnect()


app = FastAPI(lifespan=lifespan)
handler = Mangum(app)

NOW = datetime.now()


@app.get("/", status_code=status.HTTP_200_OK, tags=["App Info"])
def get_app_info() -> dict[str, str]:
    """Print info on app."""
    return {"info": "WhatsApp Bot", "app_version": get_env("APP_VERSION")}


app.include_router(messages.router, tags=["Messages"])

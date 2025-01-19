"""Main module for FastAPI app."""

from contextlib import asynccontextmanager
from datetime import datetime
from os import getenv

import ngrok
from fastapi import FastAPI, status
from mangum import Mangum

from backend.routers.messages import messages

from .auth import NGROK_AUTH_TOKEN, NGROK_DOMAIN

TZ = getenv("TZ", "UTC")


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
handler = Mangum(app)
NOW = datetime.now(TZ)


@app.get("/", status_code=status.HTTP_200_OK, tags=["App Info"])
def get_app_info() -> dict[str, str]:
    """Print info on app."""
    return {"info": "WhatsApp Bot", "app_version": "0.0.1"}


app.include_router(messages.router, tags=["Messages"])

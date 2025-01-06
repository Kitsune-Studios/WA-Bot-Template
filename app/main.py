from fastapi import FastAPI, status
import ngrok
from contextlib import asynccontextmanager

from mangum import Mangum
from datetime import datetime
from app.routers.messages import messages
from .auth import NGROK_DOMAIN, NGROK_AUTH_TOKEN

APPLICATION_PORT = 8000


@asynccontextmanager
async def lifespan(app: FastAPI):
    print(f"Setting up Ngrok Tunnel on {NGROK_DOMAIN}")
    ngrok.set_auth_token(NGROK_AUTH_TOKEN)
    ngrok.forward(
        addr=APPLICATION_PORT,
        domain=NGROK_DOMAIN,
    )
    yield
    print("Tearing Down Ngrok Tunnel")
    ngrok.disconnect()


app = FastAPI(lifespan=lifespan)
handler = Mangum(app)
NOW = datetime.now()


@app.get("/", status_code=status.HTTP_200_OK, tags=["App Info"])
def get_app_info():
    """Print info on app"""
    return {"info": "WhatsApp Bot", "app_version": "0.0.1"}


app.include_router(messages.router, tags=["Messages"])

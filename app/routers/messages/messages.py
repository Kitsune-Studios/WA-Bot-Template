from fastapi import APIRouter, Request, status
from fastapi.responses import PlainTextResponse

from app.auth import VERIFY_TOKEN
from app.routers.utils import get_wa_data, is_user_message
from app.services.messaging import send_message

from .templates import hello_world

router = APIRouter()


@router.get("/message", status_code=status.HTTP_200_OK)
async def subscribe(request: Request):
    print("subscribe is being called")

    if request.query_params.get("hub.verify_token") == VERIFY_TOKEN:
        return PlainTextResponse(request.query_params.get("hub.challenge"))
    return "Authentication failed. Invalid Token."


@router.post("/message", status_code=status.HTTP_200_OK)
async def reply(request: Request):
    wa_data = await request.json()

    # Check if it comes from user or system
    if not is_user_message(wa_data):
        return

    username, number, message, conversation_id = get_wa_data(wa_data)

    text = hello_world(username)

    send_message(number, text)

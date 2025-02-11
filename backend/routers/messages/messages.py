"""Routes for handling messages."""

from os import getenv

from fastapi import APIRouter, HTTPException, Request, status
from fastapi.responses import PlainTextResponse

from backend.routers.utils import get_wa_data, is_user_message
from backend.schemas.message_templates import TemplateRequest
from backend.services.messaging import format_template_message_input, send_message

from .templates import hello_world

router = APIRouter()


@router.get("/message", status_code=status.HTTP_200_OK)
async def subscribe(request: Request) -> str:
    """Subscribe to the WhatsApp webhook."""
    if request.query_params.get("hub.verify_token") == getenv("VERIFY_TOKEN"):
        return PlainTextResponse(request.query_params.get("hub.challenge"))
    return "Authentication failed. Invalid Token."


@router.post("/message", status_code=status.HTTP_200_OK)
async def reply(request: Request) -> None:
    """Reply to a user's message."""
    wa_data = await request.json()

    # Check if it comes from user or system
    if not is_user_message(wa_data):
        return

    username, number, message, conversation_id = get_wa_data(wa_data)

    text = hello_world(username)

    send_message(number, text)


@router.post("/template", status_code=status.HTTP_202_ACCEPTED)
async def send_template(template_req: TemplateRequest) -> dict[str, str]:
    """Send a template message to a WhatsApp number.

    Args:
        template_req: Validated template request containing recipient and
            template details

    Returns:
        dict: Status of the template message send operation

    Raises:
        HTTPException: If the template message fails to send

    """

    def handle_failed_template() -> None:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="Failed to send template message",
        )

    try:
        message_input = format_template_message_input(
            template_req.recipient,
            template_req.template_name,
        )
        response = send_message(template_req.recipient, message_input)
        if response.status_code != 200:
            handle_failed_template()
        else:
            return {"status": "Template message queued for delivery"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        ) from e

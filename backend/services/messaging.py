"""Provides functions to send messages via the WhatsApp Business API."""

import json
from os import getenv

import requests

HEADERS = {
    "Content-type": "application/json",
    "Authorization": f"Bearer {getenv('ACCESS_TOKEN')}",
}
URL = f"https://graph.facebook.com/{getenv('VERSION')}/{getenv('PHONE_NUMBER_ID')}/messages"

STATUS_OK = 200


def format_text_message_input(recipient: str, text: str) -> str:
    """Format a text message input for WhatsApp messaging.

    Args:
        recipient (str): The recipient's phone number in international format.
        text (str): The text message to be sent.

    Returns:
        str: A JSON string formatted for WhatsApp messaging.

    """
    return json.dumps(
        {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": recipient,
            "type": "text",
            "text": {"preview_url": False, "body": text},
        },
    )


def format_template_message_input(recipient: str, template_name: str) -> str:
    """Format a message input for a WhatsApp template message.

    Args:
        recipient (str): The recipient's phone number in international format.
        template_name (str): The name of the template to be used.

    Returns:
        str: A JSON string representing the formatted message input.

    """
    return json.dumps(
        {
            "messaging_product": "whatsapp",
            "to": recipient,
            "type": "template",
            "template": {"name": template_name, "language": {"code": "en"}},
        },
    )


def send_message(recipient: str, text: str) -> requests.Response:
    """Send a WhatsApp message to a specified recipient using the WhatsApp Business API.

    It sends a text message via WhatsApp Business API to a specified phone number.

    recipient (str): The phone number of the recipient in international format \
        (e.g. "521234567890")
    text (str): The text message content to be sent

    requests.Response: The HTTP response from the WhatsApp API request.
    Contains status_code and response data indicating success or failure.
    """
    message = format_text_message_input(recipient, text)

    response = requests.post(URL, data=message, headers=HEADERS)
    if response.status_code == STATUS_OK:
        return response
    return response

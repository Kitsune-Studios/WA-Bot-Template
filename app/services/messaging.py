import json

import requests

from app.auth import ACCESS_TOKEN, PHONE_NUMBER_ID, VERSION

HEADERS = {
    "Content-type": "application/json",
    "Authorization": f"Bearer {ACCESS_TOKEN}",
}
URL = f"https://graph.facebook.com/{VERSION}/{PHONE_NUMBER_ID}/messages"


def format_text_message_input(recipient: str, text: str) -> str:
    return json.dumps(
        {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": recipient,
            "type": "text",
            "text": {"preview_url": False, "body": text},
        }
    )


def format_template_message_input(recipient: str, template_name: str) -> str:
    return json.dumps(
        {
            "messaging_product": "whatsapp",
            "to": recipient,
            "type": "template",
            "template": {"name": template_name, "language": {"code": "en"}},
        }
    )


def send_message(recipient: str, text: str):

    message = format_text_message_input(recipient, text)

    response = requests.post(URL, data=message, headers=HEADERS)
    if response.status_code == 200:
        print("Status:", response.status_code)
        print("Content-type:", response.headers["content-type"])
        print("Body:", response.text)
        return response
    else:
        print(response.status_code)
        print(response.text)
        return response

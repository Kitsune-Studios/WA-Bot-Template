"""Test fixtures for API testing."""

from typing import Any


# WhatsApp message webhook example fixtures
def whatsapp_text_message_fixture() -> dict[str, Any]:
    """Create a fixture for WhatsApp text message webhook."""
    return {
        "object": "whatsapp_business_account",
        "entry": [
            {
                "id": "WHATSAPP_BUSINESS_ACCOUNT_ID",
                "changes": [
                    {
                        "value": {
                            "messaging_product": "whatsapp",
                            "metadata": {
                                "display_phone_number": "1234567890",
                                "phone_number_id": "PHONE_NUMBER_ID",
                            },
                            "contacts": [
                                {
                                    "profile": {
                                        "name": "Test User",
                                    },
                                    "wa_id": "SENDER_WHATSAPP_ID",
                                },
                            ],
                            "messages": [
                                {
                                    "from": "SENDER_WHATSAPP_ID",
                                    "id": "MESSAGE_ID",
                                    "timestamp": "1234567890",
                                    "text": {
                                        "body": "Hello, World!",
                                    },
                                    "type": "text",
                                },
                            ],
                        },
                        "field": "messages",
                    },
                ],
            },
        ],
    }


def whatsapp_media_message_fixture() -> dict[str, Any]:
    """Create a fixture for WhatsApp media message webhook."""
    return {
        "object": "whatsapp_business_account",
        "entry": [
            {
                "id": "WHATSAPP_BUSINESS_ACCOUNT_ID",
                "changes": [
                    {
                        "value": {
                            "messaging_product": "whatsapp",
                            "metadata": {
                                "display_phone_number": "1234567890",
                                "phone_number_id": "PHONE_NUMBER_ID",
                            },
                            "contacts": [
                                {
                                    "profile": {
                                        "name": "Test User",
                                    },
                                    "wa_id": "SENDER_WHATSAPP_ID",
                                },
                            ],
                            "messages": [
                                {
                                    "from": "SENDER_WHATSAPP_ID",
                                    "id": "MESSAGE_ID",
                                    "timestamp": "1234567890",
                                    "type": "image",
                                    "image": {
                                        "mime_type": "image/jpeg",
                                        "sha256": "IMAGE_HASH",
                                        "id": "IMAGE_ID",
                                    },
                                },
                            ],
                        },
                        "field": "messages",
                    },
                ],
            },
        ],
    }

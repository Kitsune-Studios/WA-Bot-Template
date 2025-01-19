"""Utility functions for the WhatsApp webhook router."""


def is_user_message(data: dict) -> bool | None:
    """Check if the WhatsApp webhook payload contains user data.

    Args:
        data (dict): a python dictionary containing the WhatsApp webhook payload.

    Returns:
        bool | None: a boolean value indicating if the payload contains user data.

    """
    try:
        data["entry"][0]["changes"][0]["value"]["contacts"]
    except KeyError:
        return False
    else:
        return True


def get_wa_data(wa_data: dict) -> tuple[str, str, str, str]:
    """Get the necessary data from the WhatsApp webhook payload.

    Args:
        wa_data (dict): a python dictionary containing the WhatsApp webhook payload.

    Returns:
        tuple[str, str, str, str]: a tuple containing the username, number,
        message, and conversation_id.

    """
    data = wa_data["entry"][0]
    conversation_data = data["changes"][0]["value"]

    conversation_id = data["id"]

    contacts_data = conversation_data["contacts"][0]
    message_data = conversation_data["messages"][0]

    username = contacts_data["profile"]["name"]
    number = contacts_data["wa_id"]
    message = (
        message_data.get("text", {}).get("body")
        if "text" in message_data
        else message_data.get("button").get("text")
    )

    return username, number, message, conversation_id

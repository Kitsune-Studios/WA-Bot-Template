def is_user_message(data):
    try:
        data["entry"][0]["changes"][0]["value"]["contacts"]
        return True
    except KeyError:
        return False


def get_wa_data(wa_data):
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

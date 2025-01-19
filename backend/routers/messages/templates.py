"""Pydantic models for the messages templates."""


def hello_world(username: str) -> str:
    """Return a test message."""
    return f"""Hello {username}. This is a test message"""

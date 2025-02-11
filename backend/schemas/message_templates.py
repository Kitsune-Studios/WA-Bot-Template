"""Pydantic models for message template validation."""

from pydantic import BaseModel, Field


class TemplateRequest(BaseModel):
    """Request model for template messages.

    Args:
        recipient: The WhatsApp number to send the template to
        template_name: Name of the template to use
        language_code: ISO language code for template localization

    """

    recipient: str = Field(..., pattern=r"^\d+$", description="WhatsApp number")
    template_name: str = Field(..., min_length=1, description="Template name")
    language_code: str = Field(
        default="en",
        pattern=r"^[a-z]{2}$",
        description="ISO language code",
    )

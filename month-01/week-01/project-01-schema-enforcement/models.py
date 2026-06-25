from typing import Any

from pydantic import BaseModel, Field


class GenerateRequest(BaseModel):
    """
    Data model for the request to generate a structured response based on a given schema.
    Attributes:
        prompt (str): The input prompt to provide to the model.
        schema (dict[str, Any]): The schema defining the expected structure of the output.
        system_prompt (str): The system prompt to guide the model's behavior.
    """

    prompt: str

    schema: dict[str, Any] = Field(description="A valid JSON Schema")

    system_prompt: str = Field(
        default="Return ONLY JSON that matches the provided schema.",
        description="A system prompt to guide the model's behavior.",
    )

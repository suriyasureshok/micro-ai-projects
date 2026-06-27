from pydantic import BaseModel, Field


class GenerateResponse(BaseModel):
    """
    Response model for the AI agent's output.
    Attributes:
        output (str): The generated response from the AI agent.
    """

    output: str = Field(..., description="The generated response from the AI agent.")


class GenerateRequest(BaseModel):
    """
    Request model for generating a response from the AI agent.
    Attributes:
        prompt (str): The input prompt for the AI agent.
        schema (dict, optional): The schema to enforce on the generated response.
    """

    prompt: str = Field(..., description="The input prompt for the AI agent.")
    schema: dict = Field(
        default=None, description="The schema to enforce on the generated response."
    )

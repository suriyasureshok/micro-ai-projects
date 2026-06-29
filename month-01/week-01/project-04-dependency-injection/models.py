from pydantic import BaseModel, Field


class UserSession(BaseModel):
    """
    Represents the authenticated user's session data.
    """

    user_id: int = Field(..., description="Unique user ID.")
    username: str = Field(..., description="Username.")
    account_type: str = Field(..., description="Account type.")
    balance: float = Field(..., description="Current account balance.")


class GenerateRequest(BaseModel):
    """
    Request model for generating a response.
    """

    prompt: str = Field(..., description="The user's prompt.")


class GenerateResponse(BaseModel):
    """
    Response returned by the AI.
    """

    output: str = Field(..., description="The AI's response.")

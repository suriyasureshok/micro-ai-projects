from fastapi import FastAPI
from pydantic import BaseModel

from router import route_request

app = FastAPI(
    title="Semantic Router API",
    description="Routes user prompts to specialized AI agents.",
    version="1.0.0",
)


class PromptRequest(BaseModel):
    prompt: str


class PromptResponse(BaseModel):
    response: str
    agent_used: str


@app.post("/generate", response_model=PromptResponse)
async def generate(request: PromptRequest) -> PromptResponse:
    """
    Route the user's prompt to the appropriate AI agent.
    """

    result = await route_request(request.prompt)

    return PromptResponse(
        response=result.response,
        agent_used=result.agent_used,
    )

from typing import Any

from fastapi import FastAPI

from ai import generate_response
from models import GenerateRequest, GenerateResponse

app = FastAPI(
    title="Native Tool Calling API",
    description="An API to demonstrate native tool calling using a language model.",
    version="1.0.0",
)


@app.post("/generate")
async def generate(req: GenerateRequest) -> GenerateResponse:
    """
    Generate a response based on the provided prompt.
    Arguments:
        prompt (str): The input prompt for the AI agent.
    Returns:
        dict[str, any]: The generated response from the AI agent.
    """
    response = await generate_response(prompt=req.prompt)
    return GenerateResponse(output=response)

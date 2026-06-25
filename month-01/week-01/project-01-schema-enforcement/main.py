import os

from ai import generate_response
from dotenv import load_dotenv
from fastapi import FastAPI
from models import GenerateRequest
from pydantic_ai.models.google import GoogleModel
from pydantic_ai.providers.google import GoogleProvider

load_dotenv()

provider = GoogleProvider(
    api_key=os.getenv("GEMINI_API_KEY"),
)

model = GoogleModel(
    "gemini-3.1-flash-lite",
    provider=provider,
)

app = FastAPI(
    title="Schema Enforcer API",
    description="An API to generate structured responses based on a given schema using a language model.",
    version="1.0.0",
)


@app.post("/generate")
async def generate(req: GenerateRequest) -> dict[str, any]:
    """
    Generate a response based on the provided prompt, schema, and system prompt.
    Arguments:
        req (GenerateRequest): The request containing the prompt, schema, and system prompt.
    Returns:
        dict[str, any]: The generated response structured according to the provided schema.
    """
    response = await generate_response(
        model=model,
        prompt=req.prompt,
        schema=req.schema,
        system_prompt=req.system_prompt,
    )

    return response


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)

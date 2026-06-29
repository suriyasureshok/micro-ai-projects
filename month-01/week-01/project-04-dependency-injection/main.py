from fastapi import FastAPI

from ai import generate_response
from models import GenerateRequest, GenerateResponse, UserSession

app = FastAPI(
    title="Dependency Injection with Pydantic AI",
    description="Demonstrates runtime dependency injection using RunContext.",
    version="1.0.0",
)


@app.post("/generate")
async def generate(req: GenerateRequest) -> GenerateResponse:
    """
    Generate a response using the injected user session.
    """

    session = UserSession(
        user_id=1,
        username="Master",
        account_type="Premium",
        balance=120000.0,
    )

    response = await generate_response(
        prompt=req.prompt,
        session=session,
    )

    return GenerateResponse(output=response)

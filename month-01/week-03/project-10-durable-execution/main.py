from fastapi import FastAPI
from pydantic import BaseModel

from ai import agent


app = FastAPI(
    title="Durable AI Fallback API",
    description="Demonstrates cross-provider model fallback.",
    version="1.0.0",
)


class PromptRequest(BaseModel):
    prompt: str


class PromptResponse(BaseModel):
    response: str


@app.post("/generate", response_model=PromptResponse)
async def generate(request: PromptRequest) -> PromptResponse:

    result = await agent.run(request.prompt)

    return PromptResponse(
        response=result.output,
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8080)

import os
from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.models.fallback import FallbackModel
from pydantic_ai.models.google import GoogleModel
from pydantic_ai.providers.google import GoogleProvider
from pydantic_ai.models.openrouter import OpenRouterModel
from pydantic_ai.providers.openrouter import OpenRouterProvider

load_dotenv()


google_provider = GoogleProvider(
    api_key=os.getenv("GOOGLE_API_KEY"),
)

primary_model = GoogleModel(
    "gemini-3.1-flash-lite",
    provider=google_provider,
)

openrouter_provider = OpenRouterProvider(
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

fallback_model = OpenRouterModel(
    "openrouter/free",
    provider=openrouter_provider,
)

model = FallbackModel(
    primary_model,
    fallback_model,
)

agent = Agent(
    model=model,
    system_prompt="""
You are a knowledgeable AI assistant.

Answer user questions clearly and accurately.
""",
)

import os

from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.models.google import GoogleModel
from pydantic_ai.providers.google import GoogleProvider


load_dotenv()


provider = GoogleProvider(
    api_key=os.getenv("GOOGLE_API_KEY"),
)

model = GoogleModel(
    "gemini-3.1-flash-lite",
    provider=provider,
)

agent = Agent(
    model=model,
    system_prompt="""
You are a helpful AI assistant.

Answer user questions clearly and remember information
from the provided conversation history.
""",
)

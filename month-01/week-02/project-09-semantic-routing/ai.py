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

math_agent = Agent(
    model=model,
    system_prompt="""
You are a mathematics expert.

Solve mathematical problems accurately.
Show calculations whenever appropriate.
Do not answer questions unrelated to mathematics.
""",
)

creative_agent = Agent(
    model=model,
    system_prompt="""
You are a creative writing assistant.

Write engaging stories, poems, articles, and other creative content.
Do not answer mathematical or factual questions.
""",
)

knowledge_agent = Agent(
    model=model,
    system_prompt="""
You are a knowledgeable assistant.

Answer factual questions clearly and accurately.
Explain concepts in a simple and structured manner.
Do not generate creative writing unless explicitly asked.
""",
)

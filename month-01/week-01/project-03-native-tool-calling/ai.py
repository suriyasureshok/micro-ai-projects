import os

from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.models.google import GoogleModel
from pydantic_ai.providers.google import GoogleProvider

from tools import calculate_gst, calculate_tax

load_dotenv()

SYSTEM_PROMPT = """
You are a helpful financial assistant.

Use the available tools whenever a calculation is requested.
Do not perform mathematical calculations yourself.
"""

provider = GoogleProvider(
    api_key=os.getenv("GOOGLE_API_KEY"),
)

model = GoogleModel(
    "gemini-3.1-flash-lite",
    provider=provider,
)

agent = Agent(
    model=model,
    system_prompt=SYSTEM_PROMPT,
)

agent.tool(calculate_tax)
agent.tool(calculate_gst)


async def generate_response(prompt: str) -> str:
    """
    Executes the AI agent and returns the final response.
    """
    result = await agent.run(prompt)
    return result.output

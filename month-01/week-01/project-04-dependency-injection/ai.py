import os

from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.models.google import GoogleModel
from pydantic_ai.providers.google import GoogleProvider

from models import UserSession
from tools import get_account_type, get_balance, get_username

load_dotenv()

SYSTEM_PROMPT = """
You are a helpful account assistant.

Whenever the user asks about their account, profile, or balance,
always use the available tools instead of making assumptions.
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
    deps_type=UserSession,
)

agent.tool(get_username)
agent.tool(get_account_type)
agent.tool(get_balance)


async def generate_response(prompt: str, session: UserSession) -> str:
    """
    Executes the AI agent and returns the final response.
    """
    result = await agent.run(prompt, deps=session)
    return result.output

import os

from dotenv import load_dotenv
from fastmcp import Client
from pydantic_ai import Agent
from pydantic_ai.models.google import GoogleModel
from pydantic_ai.providers.google import GoogleProvider
from pydantic_ai.mcp import MCPToolset

load_dotenv()

SYSTEM_PROMPT = """
You are a helpful AI assistant.

Whenever you need external information or need to perform an action,
always use the available MCP tools instead of making assumptions.
"""

provider = GoogleProvider(
    api_key=os.getenv("GOOGLE_API_KEY"),
)

model = GoogleModel(
    "gemini-3.1-flash-lite",
    provider=provider,
)

mcp_client = Client("server.py")

toolset = MCPToolset(mcp_client)

agent = Agent(
    model=model,
    system_prompt=SYSTEM_PROMPT,
    toolsets=[toolset],
)


async def generate_response(prompt: str) -> str:
    """
    Executes the AI agent and returns the generated response.
    """

    result = await agent.run(prompt)
    return result.output

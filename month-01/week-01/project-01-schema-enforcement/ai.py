from typing import Any

from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.output import StructuredDict
from pydantic_ai.providers.google import GoogleProvider

load_dotenv()


async def generate_response(
    *,
    model: str,
    prompt: str,
    schema: dict[str, Any],
    system_prompt: str,
) -> dict[str, Any]:
    """
    Generate a response using the specified model, prompt, schema, and system prompt.
    Arguments:
        model (str): The name of the model to use for generating the response.
        prompt (str): The input prompt to provide to the model.
        schema (dict[str, Any]): The schema defining the expected structure of the output.
        system_prompt (str): The system prompt to guide the model's behavior.
    Returns:
        dict[str, Any]: The generated response structured according to the provided schema.
    """

    agent = Agent(
        model,
        output_type=StructuredDict(schema),
        system_prompt=system_prompt,
    )

    result = await agent.run(prompt)

    return result.output

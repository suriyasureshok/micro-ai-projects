from enum import Enum

from pydantic import BaseModel
from pydantic_ai import Agent

from ai import creative_agent, knowledge_agent, math_agent


class Route(str, Enum):
    MATH = "math"
    CREATIVE = "creative"
    KNOWLEDGE = "knowledge"


class RouterResponse(BaseModel):
    response: str
    agent_used: str


router_agent = Agent(
    model=math_agent.model,
    output_type=Route,
    system_prompt="""
You are an AI request router.

Your only responsibility is to classify the user's request into exactly one category.

Categories:

- math
- creative
- knowledge

Return ONLY one category.
""",
)


async def route_request(prompt: str) -> RouterResponse:

    route = await router_agent.run(prompt)

    match route.output:
        case Route.MATH:
            result = await math_agent.run(prompt)

        case Route.CREATIVE:
            result = await creative_agent.run(prompt)

        case Route.KNOWLEDGE:
            result = await knowledge_agent.run(prompt)

    print(type(result.output))
    print(result.output)

    return RouterResponse(
        response=result.output,
        agent_used=route.output.value,
    )

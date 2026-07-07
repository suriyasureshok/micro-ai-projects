import asyncio

from ai import generate_response


async def main() -> None:
    """
    Entry point of the application.
    """

    print("=" * 50)
    print("Project 8 - End-to-End MCP Orchestration")
    print("=" * 50)

    prompt = input("\nEnter your prompt: ")

    response = await generate_response(prompt)

    print("\nAI Response:\n")
    print(response)


if __name__ == "__main__":
    asyncio.run(main())

import asyncio

from pydantic_ai import ModelMessage

from ai import agent


async def main() -> None:
    message_history: list[ModelMessage] = []

    print("AI Chatbot")
    print("Type 'exit' to stop.\n")

    while True:
        user_prompt = input("You: ")

        if user_prompt.lower() == "exit":
            break

        result = await agent.run(
            user_prompt,
            message_history=message_history,
        )

        message_history.extend(
            result.new_messages(),
        )

        print(f"AI: {result.output}")
        print(f"Messages stored: {len(message_history)}\n")


if __name__ == "__main__":
    asyncio.run(main())

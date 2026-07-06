import asyncio

from client import run_client


async def main() -> None:
    """
    Entry point of the application.
    """
    await run_client()


if __name__ == "__main__":
    asyncio.run(main())

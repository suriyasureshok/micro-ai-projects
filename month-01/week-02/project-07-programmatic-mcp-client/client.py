from fastmcp import Client


async def run_client() -> None:
    """
    Connects to the MCP server and demonstrates
    tool discovery and execution.
    """
    async with Client("server.py") as client:
        print("\nConnected to the MCP server.\n")

        # List available tools
        tools = await client.list_tools()

        print("Available Tools:\n")

        for tool in tools:
            print(f"- {tool.name}: {tool.description}")

        print()

        # Execute current_time tool
        result = await client.call_tool("current_time")

        print("Current Time:")
        print(result)

        print()

        # Execute server_status tool
        result = await client.call_tool("server_status")

        print("Server Status:")
        print(result)

        print()

        # Execute add_numbers tool
        result = await client.call_tool(
            "add_numbers",
            {
                "a": 25,
                "b": 17,
            },
        )

        print("Addition Result:")
        print(result)

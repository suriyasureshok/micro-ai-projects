from datetime import datetime

from fastmcp import FastMCP

mcp = FastMCP("MCP Server")


@mcp.tool
def current_time() -> str:
    """
    Returns the current local time.
    """
    return datetime.now().strftime("%I:%M:%S %p")


@mcp.tool
def server_status() -> str:
    """
    Returns the current status of the server.
    """
    return "Server is running successfully."


@mcp.tool
def add_numbers(a: float, b: float) -> float:
    """
    Adds two numbers together.
    """
    return a + b


if __name__ == "__main__":
    mcp.run()

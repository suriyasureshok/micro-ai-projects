from fastmcp import FastMCP
from datetime import datetime


mcp = FastMCP("Sandbox Server")


@mcp.tool()
async def current_time() -> str:
    """Returns the current server time in ISO 8601 format."""
    return datetime.now().isoformat()


@mcp.tool()
async def server_status() -> dict:
    """Returns the current server status."""
    return {
        "status": "running",
        "uptime": "24 hours",
    }


if __name__ == "__main__":
    mcp.run()

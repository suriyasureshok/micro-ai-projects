from datetime import datetime
from fastmcp import FastMCP

mcp = FastMCP("MCP Server")


@mcp.tool
def current_time() -> str:
    """Get the current time."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


@mcp.tool
def book_ticket(destination: str, date: str) -> str:
    """Book a ticket to a destination on a specific date."""
    return f"Ticket booked to {destination} on {date}."


if __name__ == "__main__":
    mcp.run()

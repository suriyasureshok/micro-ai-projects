from datetime import datetime

from fastmcp import FastMCP

mcp = FastMCP("Progressive Disclosure Server")


# -----------------------------
# Tool
# -----------------------------
@mcp.tool
def current_time() -> str:
    """Return the current server time."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# -----------------------------
# Resource
# -----------------------------
@mcp.resource("config://app")
def app_config() -> dict:
    """Read-only application configuration."""
    return {
        "app_name": "AI Infrastructure",
        "version": "1.0.0",
        "environment": "development",
        "owner": "Suriya",
    }


# -----------------------------
# Prompt
# -----------------------------
@mcp.prompt
def summarize_code(language: str = "Python") -> str:
    """Reusable prompt for summarizing code."""
    return f"""
You are an expert {language} software engineer.

Analyze the provided source code and explain:

1. Purpose of the code
2. Overall workflow
3. Important functions
4. Possible improvements

Keep the explanation beginner friendly.
"""


if __name__ == "__main__":
    mcp.run()

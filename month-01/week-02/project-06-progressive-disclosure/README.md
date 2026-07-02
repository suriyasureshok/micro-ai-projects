# Project 6: Progressive Disclosure via MCP Resources

## Overview

While MCP Tools allow AI systems to execute actions, not every interaction requires computation. Many AI applications simply need access to structured information or reusable instructions. The **Model Context Protocol (MCP)** addresses this by introducing **Resources** and **Prompts**, enabling AI clients to retrieve context only when it is actually needed.

This project expands the FastMCP server built in the previous project by exposing both **read-only Resources** and reusable **Prompt Templates** alongside traditional MCP Tools.

By separating executable actions from contextual information, MCP enables **progressive disclosure**, allowing AI systems to dynamically fetch relevant context instead of embedding large amounts of information into every request.

---

## Objective

Build a Python application that:

* Creates a standalone FastMCP server
* Exposes executable MCP Tools
* Publishes read-only MCP Resources
* Defines reusable MCP Prompt Templates
* Demonstrates progressive context loading
* Explores the differences between Tools, Resources, and Prompts

---

## Example Components

### MCP Tool

```python
@mcp.tool
def current_time():
    """Return the current server time."""
    ...
```

Executes a Python function and returns its result.

---

### MCP Resource

```python
@mcp.resource("config://app")
def app_config():
    ...
```

Exposes static, read-only application data that clients can retrieve whenever required.

---

### MCP Prompt

```python
@mcp.prompt
def summarize_code(language: str):
    ...
```

Provides reusable prompt templates that AI clients can dynamically load instead of embedding lengthy prompts into every request.

---

## Project Structure

```text
project-06-progressive-disclosure/
│
├── main.py
├── pyproject.toml
├── README.md
└── .python-version
```

The project intentionally remains lightweight, focusing exclusively on understanding the three primary MCP primitives.

---

## How It Works

1. A FastMCP server is initialized.
2. Native Python functions are registered as MCP Tools.
3. Static application information is exposed as an MCP Resource.
4. A reusable instruction template is exposed as an MCP Prompt.
5. The server starts over the stdio transport.
6. An MCP client connects to the server.
7. The client discovers available Tools, Resources, and Prompts.
8. Resources are fetched only when requested.
9. Prompts are loaded dynamically and reused across interactions.

---

## Progressive Disclosure

Traditional AI applications often include large configuration files, documentation, or system instructions inside every prompt, unnecessarily increasing token usage.

MCP solves this by allowing clients to request contextual information only when required.

Instead of sending:

- Configuration
- Documentation
- Policies
- Prompt templates

with every request, they are exposed as MCP Resources or Prompts and fetched on demand.

This architecture significantly reduces context size while improving modularity and maintainability.

---

## Tools vs Resources vs Prompts

| Component | Purpose | Side Effects |
|-----------|----------|--------------|
| Tool | Execute actions | ✅ Yes |
| Resource | Read contextual information | ❌ No |
| Prompt | Provide reusable instructions | ❌ No |

Each serves a distinct responsibility within an MCP server, enabling a clean separation between execution, context retrieval, and prompt engineering.

---

## Applications

This architecture is commonly used for:

* Configuration management
* Documentation retrieval
* Database schema exposure
* API specifications
* Coding guidelines
* Internal knowledge bases
* Reusable prompt libraries
* Enterprise AI assistants

---

## Key Takeaways

This project introduces two additional building blocks of the Model Context Protocol beyond executable tools. By exposing Resources and Prompts, AI systems can retrieve only the information required for a specific task, implementing the principle of progressive disclosure. This approach reduces token consumption, improves modularity, and creates scalable AI infrastructure where context is treated as an on-demand resource rather than being permanently embedded into every prompt.
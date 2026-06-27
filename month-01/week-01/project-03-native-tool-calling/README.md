# Project 3: Native Tool Calling Foundations

## Overview

Large Language Models (LLMs) excel at reasoning and generating natural language, but they should not be responsible for performing deterministic computations or interacting directly with external systems. This project demonstrates how **Pydantic AI** enables an LLM to invoke native Python functions as tools, allowing the model to delegate specialized tasks instead of attempting to generate answers itself.

Rather than calculating values internally, the LLM decides when a tool is required, calls the appropriate Python function, waits for its execution, and then incorporates the returned result into its final response. This transforms the model from a passive text generator into an intelligent orchestration layer capable of interacting with deterministic business logic.

---

## Objective

Build a Python application that:

* Creates a Pydantic AI agent
* Registers native Python functions as tools
* Allows the LLM to automatically select the appropriate tool
* Executes deterministic business logic through Python functions
* Returns a natural language response using the tool's output

---

## Example Tools

The application exposes local Python functions as tools for the agent.

```python
def calculate_tax(ctx: RunContext, income: float) -> float:
    ...

def calculate_gst(ctx: RunContext, amount: float) -> float:
    ...
```

These functions become capabilities that the language model can invoke whenever they are required to answer a user's request.

---

## Project Structure

```text
project-03-native-tool-calling/
│
├── main.py          # FastAPI application and API endpoints
├── ai.py            # Pydantic AI agent configuration and execution
├── tools.py         # Native Python tools
├── pyproject.toml
└── README.md
```

The project follows a layered architecture by separating the HTTP layer, AI orchestration layer, and business logic into independent modules.

---

## How It Works

1. The developer defines one or more Python functions that perform deterministic tasks.
2. A Pydantic AI `Agent` is created with a system prompt describing its behavior.
3. The Python functions are registered as tools using `agent.tool()`.
4. A user sends a natural language request to the FastAPI endpoint.
5. The agent analyzes the request and determines whether a tool is required.
6. If necessary, the LLM generates a structured tool call instead of continuing text generation.
7. Pydantic AI executes the corresponding Python function.
8. The returned value is provided back to the LLM.
9. The LLM synthesizes a final natural language response using the tool's output.

---

## Why Tool Calling Matters

Without tool calling, an LLM attempts to answer every question using only its internal reasoning, which can lead to inaccurate calculations and unreliable interactions with external systems.

Native tool calling provides several advantages:

* Enables deterministic computations
* Eliminates hallucinations for executable tasks
* Separates AI reasoning from business logic
* Allows seamless integration with existing Python code
* Makes AI systems extensible through reusable tools
* Forms the foundation of modern AI agent architectures

---

## Applications

This pattern is widely used for:

* Financial calculations
* Database queries
* Weather and stock lookups
* Email and notification services
* Calendar and scheduling assistants
* API integrations
* File management
* Enterprise AI agents
* AI-powered backend services

---

## Key Takeaways

Native tool calling is one of the fundamental building blocks of modern AI agents. Instead of expecting the language model to solve every problem independently, the model learns to recognize when external functionality is required and delegates execution to specialized Python functions. This separation of reasoning and execution produces AI systems that are more reliable, deterministic, maintainable, and capable of integrating with real-world software infrastructure.

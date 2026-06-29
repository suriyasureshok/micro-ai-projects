# Project 4: Dependency Injection with Pydantic AI

## Overview

Large Language Models (LLMs) often require access to runtime-specific information such as authenticated users, database connections, API clients, or configuration objects. Embedding this information directly into prompts or relying on global variables quickly becomes unmaintainable and prevents applications from scaling safely.

This project demonstrates how **Pydantic AI** uses **Dependency Injection** to provide runtime context to AI agents through `deps_type` and `RunContext`.

Instead of hardcoding application state or exposing global objects, dependencies are injected into each agent execution, allowing tools to access request-specific information while keeping the agent itself completely stateless.

---

## Objective

Build a Python application that:

* Defines a runtime dependency using a Pydantic `BaseModel`
* Configures an agent with `deps_type`
* Injects user-specific data during agent execution
* Accesses injected dependencies through `RunContext`
* Demonstrates stateless tool execution without relying on global variables

---

## Example Dependency

The application defines a runtime user session.

```python
class UserSession(BaseModel):
    user_id: int
    username: str
    account_type: str
    balance: float
```

Rather than asking the language model to remember or infer user information, this object is injected into the agent at runtime.

---

## How It Works

1. The developer defines a runtime dependency using a Pydantic `BaseModel`.
2. The dependency model is assigned to the agent through the `deps_type` parameter.
3. The application creates a `UserSession` object for the current request.
4. The dependency is passed to the agent using the `deps` argument during execution.
5. Pydantic AI makes the dependency available through `RunContext`.
6. Agent tools access the injected dependency using `ctx.deps`.
7. The language model invokes the appropriate tool whenever user-specific information is required.
8. The tool returns the requested data, which the language model incorporates into its final response.

---

## Why Dependency Injection Matters

Without dependency injection, AI tools often rely on global variables or tightly coupled application state, making systems difficult to test, maintain, and scale.

Dependency injection provides several advantages:

* Eliminates reliance on global state
* Keeps agents stateless and reusable
* Enables safe concurrent execution
* Improves testability through dependency mocking
* Separates application logic from runtime state
* Supports scalable multi-user AI applications

---

## Applications

This pattern is commonly used for:

* Authenticated AI assistants
* Customer support systems
* Banking and financial assistants
* Multi-tenant AI applications
* Database-backed AI services
* Enterprise AI platforms
* Backend microservices using AI agents

---

## Key Takeaways

Dependency Injection is a fundamental backend engineering pattern that allows runtime-specific information to be supplied to an AI agent without coupling the agent to application state. By combining `deps_type` with `RunContext`, Pydantic AI enables tools to access strongly typed dependencies while keeping agents stateless, reusable, and safe for concurrent execution. This pattern forms the foundation for building production-ready AI systems that serve multiple users reliably.

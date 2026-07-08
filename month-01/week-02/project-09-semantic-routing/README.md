# Project 9: Semantic Routing for Compute Optimization

## Overview

Modern AI applications rarely rely on a single general-purpose agent to handle every user request. Instead, they first determine the user's intent and then route the request to a specialized agent best suited for the task.

This project demonstrates how to build a simple **semantic router** using **Pydantic AI**. A lightweight router agent classifies a user's prompt into predefined categories such as mathematics, creative writing, or general knowledge. Based on the classification, the application forwards the request to the corresponding specialized AI agent.

By separating intent classification from task execution, this architecture improves scalability, reduces unnecessary computation, and closely resembles how production AI systems optimize latency and infrastructure costs.

---

## Objective

Build a FastAPI application that:

- Creates a lightweight AI router
- Classifies user prompts into predefined categories
- Dispatches requests to specialized AI agents
- Returns both the generated response and the selected agent
- Demonstrates semantic routing as a compute optimization strategy

---

## Project Structure

```text
project-09-semantic-routing/
│
├── ai.py
├── router.py
├── main.py
├── pyproject.toml
├── README.md
└── .env
```

---

## How It Works

1. The user sends a prompt to the FastAPI endpoint.
2. The Router Agent classifies the prompt into a predefined category.
3. The router selects the appropriate specialized agent.
4. The selected agent processes the request.
5. The generated response and the selected agent are returned to the client.

---

## Architecture

```text
                     User
                       │
                       ▼
                FastAPI Endpoint
                       │
                       ▼
                 Router Agent
                       │
         ┌─────────────┼─────────────┐
         ▼             ▼             ▼
    Math Agent   Creative Agent  Knowledge Agent
         │             │             │
         └─────────────┼─────────────┘
                       ▼
                JSON Response
```

---

## Execution Flow

Suppose the user sends:

> Solve 25 × 47.

The following sequence occurs:

```text
User Prompt
      │
      ▼
Router Agent
      │
      ▼
Classifies request as "math"
      │
      ▼
Math Agent
      │
      ▼
Performs calculation
      │
      ▼
Returns response
      │
      ▼
FastAPI
      │
      ▼
{
    "response": "25 × 47 = 1175",
    "agent_used": "math"
}
```

The router never attempts to solve the problem itself. Its only responsibility is determining **which specialized agent should handle the request**.

---

## Why Semantic Routing?

Without semantic routing, every request is typically processed by the same AI agent.

```text
             User Requests
                    │
                    ▼
          General Purpose Agent
                    │
                    ▼
              Final Response
```

Although simple, this approach becomes increasingly inefficient as applications grow.

Using semantic routing:

```text
             User Requests
                    │
                    ▼
              Router Agent
                    │
        ┌───────────┼───────────┐
        ▼           ▼           ▼
     Math      Creative    Knowledge
      Agent       Agent        Agent
```

Only the required agent executes the request, making the system more modular and easier to extend.

---

## Why This Architecture Matters

Separating routing from execution provides several advantages:

- Reduces unnecessary AI computation
- Improves overall response latency
- Allows specialized prompts for different domains
- Simplifies future expansion with additional agents
- Keeps responsibilities clearly separated
- Mirrors production multi-agent architectures

Semantic routing is commonly used in enterprise AI systems to intelligently distribute requests before expensive reasoning models are invoked.

---

## Applications

The same architecture can power:

- Customer support assistants
- Educational tutors
- Coding assistants
- Enterprise chatbots
- Multi-agent AI systems
- AI workflow orchestration
- Internal knowledge assistants
- Domain-specific AI platforms

---

## Key Takeaways

This project demonstrates how semantic routing enables AI systems to intelligently dispatch user requests to specialized agents. Instead of relying on a single general-purpose model, a lightweight router first classifies the user's intent before selecting the most appropriate downstream agent.

By combining **Pydantic AI** with **FastAPI**, this project introduces a scalable architectural pattern where routing and task execution remain independent, making AI applications more modular, maintainable, and cost-efficient.

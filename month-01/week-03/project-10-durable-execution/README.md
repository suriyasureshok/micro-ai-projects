# Project 10: Durable Execution and Fallback Mechanics

## Overview

AI applications often depend on external model providers to process user requests. However, upstream APIs may become temporarily unavailable due to server failures, rate limits, network issues, or provider outages.

This project demonstrates how to build a resilient AI execution layer using **Pydantic AI's FallbackModel**. A primary Google Gemini model handles requests under normal conditions. If the primary model encounters a supported provider failure, the same request is automatically attempted using a secondary model through OpenRouter.

By separating fallback mechanics from the agent and API layers, the application remains simple while gaining cross-provider resiliency.

---

## Objective

Build a FastAPI application that:

- Uses Google Gemini as the primary AI model
- Uses OpenRouter as the secondary model provider
- Combines both models using `FallbackModel`
- Automatically redirects execution when the primary provider fails
- Preserves the user's request during fallback
- Demonstrates cross-provider AI resiliency

---

## Project Structure

```text
project-10-durable-execution/
│
├── ai.py
├── main.py
├── pyproject.toml
├── README.md
└── .env
```

---

## How It Works

1. The user sends a prompt to the FastAPI endpoint.
2. The AI agent executes using a `FallbackModel`.
3. The fallback model first attempts the primary Google Gemini model.
4. If the primary model succeeds, the response is immediately returned.
5. If a supported provider failure occurs, execution moves to the OpenRouter model.
6. The fallback model processes the same request.
7. The generated response is returned to the user.

---

## Architecture

```text
                       User
                         │
                         ▼
                  FastAPI Endpoint
                         │
                         ▼
                       Agent
                         │
                         ▼
                  FallbackModel
                         │
                         ▼
                 Primary Model
                  Google Gemini
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
           Success                Failure
              │                     │
              ▼                     ▼
        Return Response      OpenRouter Model
                                    │
                                    ▼
                              Return Response
```

---

## Execution Flow

Under normal conditions:

```text
User Prompt
      │
      ▼
FastAPI
      │
      ▼
Agent
      │
      ▼
FallbackModel
      │
      ▼
Google Gemini
      │
      ▼
Successful Response
      │
      ▼
User
```

If the primary provider fails:

```text
User Prompt
      │
      ▼
FastAPI
      │
      ▼
Agent
      │
      ▼
FallbackModel
      │
      ▼
Google Gemini
      │
      ▼
Provider Failure
      │
      ▼
OpenRouter
      │
      ▼
Successful Response
      │
      ▼
User
```

The agent does not manually catch provider exceptions or select another model. The fallback policy is handled by the model abstraction.

---

## Why Fallback Models?

Without fallback mechanics, application availability becomes directly dependent on a single external provider.

```text
Application
     │
     ▼
AI Provider
     │
     ▼
Provider Failure
     │
     ▼
Application Failure
```

This creates a single point of failure.

Using a fallback model:

```text
Application
     │
     ▼
FallbackModel
     │
     ├── Primary Provider
     │
     └── Secondary Provider
```

A failure in one provider does not necessarily cause the entire AI application to become unavailable.

---

## Cross-Provider Resiliency

This project deliberately uses two distinct provider paths:

```text
Primary
   │
   ▼
Google Gemini


Fallback
   │
   ▼
OpenRouter
```

The primary model communicates directly with Google's model infrastructure.

The fallback model executes through OpenRouter.

This architecture reduces tight coupling between application availability and a single upstream AI provider.

---

## Failure Policy

Fallback should be used for recoverable upstream failures such as:

- Provider server errors
- Temporary API outages
- Rate limiting
- Supported model API errors
- Certain network or service failures

Fallback should not blindly hide every application error.

Errors caused by invalid application logic, malformed local data, or programming bugs should normally propagate instead of triggering unnecessary model calls.

The fallback mechanism is therefore a **resiliency policy**, not a replacement for proper error handling.

---

## Testing the Fallback

The fallback behavior can be tested by intentionally invalidating the primary Google API key.

```env
GOOGLE_API_KEY=invalid-key
```

When a request is sent:

```text
Google Gemini
      │
      ▼
Provider Error
      │
      ▼
FallbackModel
      │
      ▼
OpenRouter
      │
      ▼
Successful Response
```

If the API still returns a generated response, cross-provider fallback has been successfully demonstrated.

---

## Why This Architecture Matters

Durable AI execution provides several advantages:

- Improves application availability
- Reduces dependency on a single model provider
- Handles temporary upstream instability
- Keeps fallback logic outside business logic
- Simplifies cross-provider model switching
- Improves infrastructure resiliency
- Reduces the impact of provider outages

The agent remains unaware of which provider ultimately processes the request.

---

## Applications

The same architecture can be used in:

- Enterprise AI assistants
- Customer support systems
- AI API platforms
- Multi-provider AI gateways
- Production chatbots
- AI workflow systems
- High-availability AI services
- Distributed AI infrastructure

---

## Key Takeaways

This project demonstrates how fallback mechanics improve the resiliency of AI applications.

Instead of directly binding an agent to a single model provider, multiple models are combined behind a `FallbackModel`. The primary model handles requests under normal conditions, while a secondary provider becomes available when supported upstream failures occur.

By combining **Pydantic AI**, **Google Gemini**, **OpenRouter**, and **FastAPI**, this project introduces a simple but important infrastructure pattern for building AI systems that remain available during provider instability.
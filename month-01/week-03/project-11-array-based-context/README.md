# Project 11: Array-Based Context Engineering

## Overview

Large language models are stateless. Each model request is an isolated execution and does not automatically remember previous conversations.

This project demonstrates how conversational context is manually managed using an array of model messages.

A command-line chatbot stores messages produced during each agent run and explicitly passes the accumulated message history back to the model on the next conversational turn.

By exposing the message history directly, the project demonstrates that conversational memory is not an intrinsic property of the model. It is an application-level context management mechanism.

---

## Objective

Build a CLI chatbot that:

- Accepts user input continuously
- Maintains an array of `ModelMessage` objects
- Passes previous messages to the model on every turn
- Appends newly generated messages to the history
- Preserves conversational context
- Displays the growth of the message history

---

## Project Structure

```text
project-11-array-context/
│
├── ai.py
├── main.py
├── pyproject.toml
├── README.md
└── .env
```

---

## How It Works

1. The application creates an empty message history.
2. The user enters a prompt.
3. The current prompt and previous message history are passed to the agent.
4. The model generates a response using the supplied context.
5. Messages generated during the current run are retrieved.
6. The new messages are appended to the message history.
7. The response is displayed to the user.
8. The process repeats with the expanded history.

---

## Architecture

```text
                    User
                      │
                      ▼
                  CLI Input
                      │
                      ▼
                    Agent
                      │
              ┌───────┴───────┐
              │               │
              ▼               ▼
        Current Prompt    Message History
              │               │
              └───────┬───────┘
                      ▼
                    Model
                      │
                      ▼
               Generated Response
                      │
                      ▼
                New Messages
                      │
                      ▼
             Append to History
                      │
                      └──────────► Next Turn
```

---

## Message History

The application begins with an empty message array:

```text
[]
```

After the first conversational turn:

```text
[
    User Message,
    Model Response
]
```

After another turn:

```text
[
    User Message,
    Model Response,
    User Message,
    Model Response
]
```

The message array continues growing for the lifetime of the application.

---

## Stateless Models

Without message history, requests are independent.

```text
Request 1
   │
   ▼
Model
   │
   ▼
Response


Request 2
   │
   ▼
Model
   │
   ▼
Response
```

The second request contains no information about the first request.

Conversation memory is created by resending previous messages:

```text
Previous Messages
        │
        ▼
Current Prompt
        │
        ▼
      Model
        │
        ▼
Context-Aware Response
```

The model appears to remember the conversation because the application reconstructs the conversation context for every request.

---

## Context Growth

Each conversational turn adds new messages to the history.

```text
Turn 1 → 2 messages
Turn 2 → 4 messages
Turn 3 → 6 messages
Turn 4 → 8 messages
```

As the conversation grows:

```text
More Messages
      │
      ▼
Larger Context Payload
      │
      ▼
More Input Tokens
      │
      ▼
Higher Processing Cost
      │
      ▼
Higher Latency
```

This demonstrates one of the fundamental infrastructure problems in long-running AI conversations.

---

## Why `new_messages()`?

The agent receives the existing history through:

```python
message_history=message_history
```

After execution, `result.new_messages()` returns only messages created during the current agent run.

```text
Existing History
       +
Current Run Messages
       │
       ▼
Updated History
```

Appending only new messages prevents previous conversation messages from being duplicated.

Using the complete message collection from every run and appending it to the existing history would repeatedly duplicate older messages.

---

## Typed Message History

The application stores:

```python
list[ModelMessage]
```

Instead of manually constructing dictionaries such as:

```text
{
    "role": "user",
    "content": "Hello"
}
```

Pydantic AI represents conversation history using typed model message objects.

This preserves framework-level message structure while still exposing the underlying context management mechanism.

---

## Testing Conversational Memory

Run the application:

```bash
uv run main.py
```

Example conversation:

```text
AI Chatbot
Type 'exit' to stop.

You: My name is Master
AI: Nice to meet you, Master.
Messages stored: 2

You: What is my name?
AI: Your name is Master.
Messages stored: 4
```

The model answers correctly because the first conversational turn is included in the message history supplied during the second request.

---

## Current Limitation

The message history grows without a limit.

```text
Conversation
      │
      ▼
Message History
      │
      ▼
More Messages
      │
      ▼
Larger Context
      │
      ▼
Increasing Token Usage
```

No messages are removed, summarized, or compressed.

For long-running conversations, this can cause:

- Increased token usage
- Higher API costs
- Increased latency
- Context window exhaustion
- Larger persistence requirements

This limitation is intentional.

The project exposes the unbounded context growth problem before introducing context constraint strategies.

---

## Relation to Sliding Windows

A basic solution is to retain only recent messages.

```text
Full History
     │
     ▼
Remove Older Messages
     │
     ▼
Recent Message Window
     │
     ▼
Model
```

However, removing older messages may cause the model to lose important information from earlier conversations.

More advanced systems combine sliding windows with conversation summarization.

These context constraint strategies are explored in the next project.

---

## Why This Architecture Matters

Array-based context management demonstrates several fundamental AI infrastructure concepts:

- Language models are stateless
- Conversation memory is application-managed
- Previous messages must be explicitly supplied
- Context payloads grow with conversation length
- Token usage increases as history expands
- Conversation history must eventually be persisted
- Context management requires explicit infrastructure policies

Understanding these mechanics is essential before using higher-level memory abstractions.

---

## Applications

The same context management pattern appears in:

- AI chatbots
- Customer support assistants
- Coding agents
- Enterprise AI assistants
- Multi-turn AI APIs
- Agent workflows
- Persistent conversation systems
- AI session management infrastructure

---

## Key Takeaways

This project demonstrates that conversational memory is fundamentally a context management problem.

The model does not retain previous requests. Instead, the application stores messages generated during each conversational turn and explicitly supplies the accumulated history during future requests.

Using Pydantic AI's `ModelMessage` objects and `message_history` interface, the project exposes the underlying mechanics of multi-turn AI conversations while preserving type-safe message structures.

The continuously growing message array also reveals the primary limitation of naive conversational memory: unbounded context growth.

This limitation provides the architectural motivation for sliding windows and summarization-based context management.

# Project 7: Programmatic MCP Client Architecture

## Overview

The Model Context Protocol (MCP) defines a standardized communication protocol between AI applications and external tools. While previous projects focused on creating MCP servers, this project shifts to the client side by demonstrating how a Python application can connect to an MCP server, discover its available tools, and execute them programmatically without involving a Large Language Model (LLM).

The project uses FastMCP's client implementation over the standard input/output (stdio) transport, exposing the complete lifecycle of an MCP connection.

---

## Objective

Build a Python application that:

- Creates an MCP client
- Connects to an MCP server over stdio
- Performs the MCP initialization handshake
- Discovers available tools
- Executes tools programmatically
- Receives and displays tool results

---

## Project Structure

```
project-07-programmatic-mcp-client/
│
├── client.py
├── server.py
├── main.py
├── pyproject.toml
└── README.md
```

---

## How It Works

1. The application starts the MCP client.
2. The client launches the MCP server using the stdio transport.
3. The client and server perform the MCP initialization handshake.
4. The server advertises its capabilities and available tools.
5. The client retrieves the list of available tools.
6. The client invokes selected tools by name.
7. The server executes the requested tool.
8. The server returns the result to the client.
9. The client displays the response.

---

## Architecture

```
               main.py
                   │
                   ▼
            run_client()
                   │
                   ▼
        FastMCP Client (stdio)
                   │
                   ▼
          FastMCP Server
                   │
      ┌────────────┼────────────┐
      ▼            ▼            ▼
 current_time   server_status  add_numbers
```

---

## Why This Matters

Modern AI systems rarely execute tools directly. Instead, they communicate with external services through standardized protocols.

A programmatic MCP client allows applications to:

- Discover available tools dynamically
- Execute tools without importing their implementations
- Communicate using a protocol rather than direct function calls
- Connect to local or remote MCP servers
- Build distributed AI systems with loosely coupled components

Understanding this client-server interaction is essential before integrating MCP with AI agents.

---

## Applications

This architecture is commonly used for:

- AI agent infrastructure
- Distributed tool execution
- Local development using stdio transport
- Remote MCP servers over HTTP or SSE
- Enterprise AI platforms
- IDE integrations
- Autonomous agent systems

---

## Key Takeaways

This project demonstrates the client side of the Model Context Protocol. Instead of relying on an AI model to invoke tools, the client communicates directly with an MCP server, performing connection setup, capability negotiation, tool discovery, and tool execution through the MCP protocol.

Understanding the MCP client lifecycle provides the foundation for building distributed AI applications where agents, tools, and execution environments remain loosely coupled through a standardized communication protocol.

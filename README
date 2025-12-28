# 🤖 Agentic AI Customer Support

A customer support chatbot application powered by n8n workflow automation and Model Context Protocol (MCP). This project demonstrates how to build an intelligent support agent that can handle order status queries and support ticket creation.

## 📸 Demo

![Application Demo](static/image.png)

## ✨ Features

- **Interactive Chat Interface**: Clean Streamlit-based UI for customer interactions
- **Order Status Tracking**: Check shipping and delivery information
- **Support Ticket Creation**: Automatically generate support tickets
- **n8n Integration**: Workflow automation powered by n8n webhooks
- **MCP Server**: FastMCP server exposing customer support tools

## 🏗️ Architecture

The project consists of two main components:

1. **MCP Server** (`server.py`): FastAPI-based MCP server with customer support tools
2. **Streamlit App** (`streamlit_app.py`): User-facing chat interface

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- n8n instance running on `localhost:5678`

### Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application

1. **Start the MCP Server**:
```bash
python server.py
```
The server will run on `http://localhost:8000/sse`

2. **Launch the Streamlit App**:
```bash
streamlit run streamlit_app.py
```

3. **Configure n8n**:
   - Set up a webhook at `http://localhost:5678/webhook/customer`
   - Connect it to the MCP server tools

## 🛠️ Available Tools

- `get_order_status(order_id)`: Retrieves shipping and delivery information
- `create_support_ticket(user_id, issue)`: Creates a support ticket

## 📝 Usage Example

User: "What's the status of order #12345?"
Agent: Uses `get_order_status` tool to fetch shipping information

User: "I need help with a refund"
Agent: Uses `create_support_ticket` to create a support ticket

## 🎓 Project Info

Agentic AI Lab - INPT 2025

## 📦 Dependencies

- `mcp`: Model Context Protocol
- `fastapi`: Web framework for MCP server
- `uvicorn`: ASGI server
- `streamlit`: UI framework
- `requests`: HTTP library

## 📄 License

Educational project for learning purposes.

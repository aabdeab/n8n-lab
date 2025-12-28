from mcp.server.fastmcp import FastMCP

# Initialize FastMCP
mcp = FastMCP("CustomerSupport")

# Lab Tools
@mcp.tool()
def get_order_status(order_id: str) -> dict:
    """Retrieves shipping and delivery information for an order."""
    return {"status": "Shipped", "delivery": "2 days"}

@mcp.tool()
def create_support_ticket(user_id: str, issue: str) -> dict:
    """Assignment 2: Creates a support ticket."""
    return {"ticket_id": f"TKT-{user_id[:3].upper()}", "status": "Created"}

if __name__ == "__main__":
    # Use the internal SSE server runner. 
    # This automatically initializes the required 'Task Group'.
    # It will run on http://localhost:8000/sse by default.
    mcp.run(transport="sse")
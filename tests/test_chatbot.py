import pytest
from src.graph import app

def run_chatbot(query: str, thread_id: str = "test_session"):
    """Helper to run chatbot and capture last assistant message."""
    config = {"configurable": {"thread_id": thread_id}}
    events = app.stream({"messages": [{"role": "user", "content": query}]}, config=config)
    last_message = None
    for event in events:
        vals = event.values()
        if "messages" in vals:
            last = vals["messages"][-1]
            if last.get("role") == "assistant":
                last_message = last.get("content")
    return last_message

def test_chatbot_basic_response():
    """Chatbot should return a response string for a simple query."""
    response = run_chatbot("Hello chatbot")
    assert isinstance(response, str)
    assert len(response) > 0

def test_chatbot_tool_routing():
    """Chatbot should attempt to call tool when query mentions applications."""
    response = run_chatbot("List project management applications")
    assert isinstance(response, str)
    # Response should mention applications or results
    assert "application" in response.lower() or "result" in response.lower()

def test_chatbot_memory_followup():
    """Chatbot should retain context across multiple queries in same thread."""
    thread_id = "memory_session"
    first = run_chatbot("What project management software is available?", thread_id=thread_id)
    followup = run_chatbot("Filter to active applications only", thread_id=thread_id)
    assert isinstance(followup, str)
    # Follow-up should not be empty and should differ from first response
    assert len(followup) > 0
    assert followup != first

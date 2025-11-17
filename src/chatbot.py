from src.graph import app

def stream_app_response(user_input: str, thread_id: str = "default_session"):
    """Stream chatbot responses with memory for a given user input."""
    config = {"configurable": {"thread_id": thread_id}}
    for event in app.stream({"messages": [{"role": "user", "content": user_input}]}, config=config):
        vals = event.values()
        if "messages" in vals:
            last = vals["messages"][-1]
            if last.get("role") == "assistant":
                print(last.get("content"))

from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, ToolNode, END
from langgraph.checkpoint.memory import MemorySaver
from langchain.tools import Tool
from src.tools import search_app_portfolio

# Define tool
snow_tool = Tool(
    name="servicenow_cmdb_app_portfolio_search",
    description="Search ServiceNow CMDB for applications",
    func=search_app_portfolio
)

# Bind tool to LLM
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
llm_with_tools = llm.bind_tools([snow_tool])

# Define graph state
class ChatState(dict):
    pass

def chatbot_node(state: ChatState) -> ChatState:
    response = llm_with_tools.invoke(state["messages"])
    return {"messages": state["messages"] + [response]}

tool_node = ToolNode(tools=[snow_tool])

def tools_condition(state: ChatState) -> str:
    last = state["messages"][-1]
    if last.get("tool_calls"):
        return "tools"
    return END

# Build graph
graph = StateGraph(ChatState)
graph.add_node("chatbot", chatbot_node)
graph.add_node("tools", tool_node)
graph.add_conditional_edges("chatbot", tools_condition, {"tools": "tools", END: END})
graph.add_edge("tools", "chatbot")
graph.set_entry_point("chatbot")

# Add memory
memory = MemorySaver()
app = graph.compile(checkpointer=memory)

# Architecture Overview — ServiceNow CMDB Chatbot

This document outlines the architecture of the tool-enabled, memory-aware chatbot designed to query ServiceNow CMDB using natural language. Built with LangGraph, the system combines tool invocation, conversational memory, and LLM reasoning to deliver accurate, context-aware responses.

---

## Core Components

### 1. Chatbot Node (`chatbot`)
- Uses an LLM (e.g., `gpt-4o-mini`) to interpret user input.
- Decides whether to respond directly or call a tool.
- Bound to tools via `llm.bind_tools()`.

### 2. Tool Node (`tools`)
- Executes queries against ServiceNow CMDB via REST API.
- Returns structured data (application name, owner, cost, department, etc.).
- Uses LangChain’s `Tool` wrapper for modularity.

### 3. Memory Node (`MemorySaver`)
- Stores conversation checkpoints.
- Enables multi-turn context retention.
- Thread ID used to isolate sessions (`"single_session_memory"` or custom).

---

## Graph Flow

START → Chatbot → (if tool call) Tools → Chatbot → Memory → END


- Conditional edge from `chatbot` checks for `tool_calls`.
- If present, routes to `tools`; otherwise ends or loops.
- Memory checkpoint ensures continuity across queries.

---

## Tool Integration

### Tool: `servicenow_cmdb_app_portfolio_search`
- Input: Natural language query (e.g., “What project management tools are available?”)
- Output: JSON with application metadata
- Fields: `name`, `owner`, `cost`, `department`, `status`, `source URL`

---

## Example Interaction

**User:**  
> What project management software is available for my department?

**Chatbot:**  
→ Calls CMDB tool  
→ Retrieves matching applications  
→ Formats response with owner, cost, and source link

**User (Follow-up):**  
> Filter to active applications and show cost centers.

**Chatbot:**  
→ Uses memory to retain context  
→ Refines query  
→ Returns updated results

---

## Extensibility

- Add more tools (e.g., HR systems, asset inventory) via LangChain `Tool` interface.
- Replace naive query parsing with function-calling schema.
- Deploy via container or cloud endpoint for enterprise use.

---

## Design Principles

- **Modular:** Each node is independently testable and replaceable.
- **Governance-aware:** Tool calls are auditable; responses include source links.
- **User-friendly:** No technical syntax required; plain language input supported.
- **Secure:** Secrets handled via `.env`; roles restrict data access.

---


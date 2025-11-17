# servicenow-cmdb-chatbot
Tool-enabled, memory-aware chatbot for querying ServiceNow CMDB with natural language.

---

```markdown
# ServiceNow CMDB Chatbot — Tool-Enabled, Memory-Aware

This project enables natural language querying of the ServiceNow CMDB application portfolio using a LangGraph-powered chatbot. 
It combines external tool calls with conversational memory to deliver accurate, context-aware responses for general users across an organization.

---

## Use Case

Empower non-technical staff to ask questions like:

> “What project management software is available for my team to use in my department? Include application owner, any costs, and other pertinent information.”

The chatbot retrieves structured data from ServiceNow CMDB and responds with clarity, continuity, and source traceability.

---

## Architecture Overview

```
START → Chatbot → Tool (ServiceNow CMDB) → Chatbot → Memory → END
```

- **LLM Node:** Generates responses and decides when to call tools
- **Tool Node:** Queries ServiceNow CMDB via REST API
- **Memory Node:** Retains conversation context across multiple turns
- **LangGraph:** Orchestrates flow between nodes

---

## Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/your-username/servicenow-cmdb-chatbot.git
cd servicenow-cmdb-chatbot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure environment variables
Create a `.env` file:
```
SNOW_INSTANCE_URL=https://your-instance.service-now.com
SNOW_USERNAME=your_username
SNOW_PASSWORD=your_password
OPENAI_API_KEY=your_openai_key
```

> ⚠Never commit `.env` files. Add `.env` to `.gitignore`.

---

## Project Structure

```
servicenow-cmdb-chatbot/
│
├── src/
│   ├── chatbot.py           # Core chatbot logic
│   ├── tools.py             # ServiceNow CMDB tool integration
│   └── graph.py             # LangGraph workflow setup
│
├── notebooks/
│   └── demo.ipynb           # Interactive demo
│
├── docs/
│   └── architecture.md      # Technical overview
│
├── tests/
│   └── test_tools.py        # Unit tests
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Example Usage

```python
stream_app_response("What project management tools are available for my department?")
stream_app_response("Filter to active applications and show cost centers.")
```

---

## Features

- Tool-enabled: Calls ServiceNow CMDB for live data
- Memory-aware: Retains context across queries
- Natural language: No technical syntax required
- Transparent: Includes source links to CMDB records
- Modular: Built with LangGraph for extensibility

---

## Future Enhancements

- Function-calling schema for better query parsing
- Role-based access control for sensitive fields
- Deployment via container or cloud endpoint
- UI overlay for non-technical users

---

## Maintainer

**Alexander Stevens**  
Strategic AI Enablement Leader  
alexstevens1969@gmail.com | Passionate about modular workflows, educational outreach, and governance-aware AI systems

---

```


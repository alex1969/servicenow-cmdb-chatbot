import os
import requests

SNOW_INSTANCE_URL = os.getenv("SNOW_INSTANCE_URL", "").rstrip("/")
SNOW_USERNAME = os.getenv("SNOW_USERNAME")
SNOW_PASSWORD = os.getenv("SNOW_PASSWORD")

def search_app_portfolio(query: str) -> dict:
    """Search ServiceNow CMDB for applications matching the query."""
    if not SNOW_INSTANCE_URL:
        return {"error": "Missing SNOW_INSTANCE_URL"}

    table = "cmdb_ci_appl"  # adjust to your schema
    url = f"{SNOW_INSTANCE_URL}/api/now/table/{table}"
    params = {
        "sysparm_query": f"nameLIKES{query}^ORshort_descriptionLIKES{query}",
        "sysparm_fields": "sys_id,name,short_description,owned_by,department,cost_center,total_cost",
        "sysparm_limit": "5"
    }

    try:
        resp = requests.get(url, params=params, auth=(SNOW_USERNAME, SNOW_PASSWORD), timeout=15)
        resp.raise_for_status()
        return {"results": resp.json().get("result", [])}
    except requests.RequestException as e:
        return {"error": str(e)}

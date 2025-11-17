import pytest
from unittest.mock import patch
from src import tools

@patch("src.tools.requests.get")
def test_search_app_portfolio_mocked(mock_get):
    """Mock ServiceNow API call to test tool behavior without live credentials."""
    # Configure mock response
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "result": [
            {
                "sys_id": "12345",
                "name": "Project Management Pro",
                "short_description": "PM tool for IT",
                "owned_by": "Jane Doe",
                "department": "IT",
                "cost_center": "CC100",
                "total_cost": "12000"
            }
        ]
    }

    result = tools.search_app_portfolio("project management")
    assert "results" in result
    assert result["results"][0]["name"] == "Project Management Pro"
    assert result["results"][0]["owned_by"] == "Jane Doe"

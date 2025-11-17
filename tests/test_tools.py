import pytest
from src import tools

def test_search_app_portfolio_returns_dict():
    """Ensure the function always returns a dictionary."""
    result = tools.search_app_portfolio("project management")
    assert isinstance(result, dict)

def test_search_app_portfolio_has_results_or_error():
    """Check that the function returns either results or an error key."""
    result = tools.search_app_portfolio("project management")
    assert "results" in result or "error" in result

def test_search_app_portfolio_empty_query():
    """Empty query should still return a dict with results or error."""
    result = tools.search_app_portfolio("")
    assert isinstance(result, dict)
    assert "results" in result or "error" in result

def test_safe_get_helper():
    """Validate safe_get utility function."""
    d = {"key": "value"}
    assert tools.safe_get(d, "key") == "value"
    assert tools.safe_get(d, "missing", default="default") == "default"

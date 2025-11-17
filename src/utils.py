import json

def pretty_print(data: dict) -> None:
    """Print JSON data in a readable format."""
    print(json.dumps(data, indent=2, ensure_ascii=False))

def safe_get(d: dict, key: str, default=None):
    """Safely get a key from a dict."""
    return d.get(key, default)

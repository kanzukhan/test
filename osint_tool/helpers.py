import json

try:
    import requests
except ImportError:  # fall back to urllib
    requests = None
import urllib.request


def fetch_json(url: str, headers: dict | None = None) -> dict:
    """Fetch JSON from a URL using requests or urllib."""
    headers = headers or {}
    if requests:
        r = requests.get(url, headers=headers, timeout=10)
        r.raise_for_status()
        return r.json()
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=10) as resp:
        return json.loads(resp.read().decode())


def fetch_text(url: str, headers: dict | None = None) -> str:
    """Fetch raw text from a URL."""
    headers = headers or {}
    if requests:
        r = requests.get(url, headers=headers, timeout=10)
        r.raise_for_status()
        return r.text
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=10) as resp:
        return resp.read().decode()

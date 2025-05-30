import os
from ..helpers import fetch_json

API_URL = "https://ipinfo.io/{ip}/json"
API_TOKEN = os.getenv("IPINFO_TOKEN")


def lookup(ip: str) -> dict:
    """Lookup IP information using ipinfo.io API."""
    url = API_URL.format(ip=ip)
    headers = {}
    if API_TOKEN:
        headers["Authorization"] = f"Bearer {API_TOKEN}"
    return fetch_json(url, headers=headers)

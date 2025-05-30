import os
from ..helpers import fetch_json

API_URL = "https://haveibeenpwned.com/api/v3/breachedaccount/{account}"
API_KEY = os.getenv("HIBP_KEY")

HEADERS = {
    "User-Agent": "osint-tool/1.0",
    "hibp-api-key": API_KEY or "",
}


def lookup(account: str) -> dict:
    """Check if an account has been breached using HaveIBeenPwned API."""
    if not API_KEY:
        raise RuntimeError("HIBP_KEY environment variable not set")
    url = API_URL.format(account=account)
    try:
        breaches = fetch_json(url, headers=HEADERS)
    except Exception as exc:
        if hasattr(exc, "code") and exc.code == 404:
            return {"breaches": []}
        raise
    return {"breaches": breaches}

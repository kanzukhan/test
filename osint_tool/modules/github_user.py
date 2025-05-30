from ..helpers import fetch_json

API_URL = "https://api.github.com/users/{user}"


def lookup(user: str) -> dict:
    """Fetch public GitHub profile information."""
    url = API_URL.format(user=user)
    return fetch_json(url)

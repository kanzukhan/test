from ..helpers import fetch_json

API_URL = "https://public-api.solscan.io/account/{address}"


def lookup(address: str) -> dict:
    """Lookup Solana wallet information via Solscan."""
    url = API_URL.format(address=address)
    return fetch_json(url)

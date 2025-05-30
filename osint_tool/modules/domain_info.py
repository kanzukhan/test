from ..helpers import fetch_json

API_URL = "https://api.domainsdb.info/v1/domains/search?domain={domain}"


def lookup(domain: str) -> dict:
    """Search domain information using domainsdb.info API."""
    url = API_URL.format(domain=domain)
    return fetch_json(url)

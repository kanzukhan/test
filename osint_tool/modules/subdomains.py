from ..helpers import fetch_text

API_URL = "https://api.hackertarget.com/hostsearch/?q={domain}"


def lookup(domain: str) -> dict:
    """Enumerate subdomains using hackertarget.com hostsearch API."""
    url = API_URL.format(domain=domain)
    text = fetch_text(url)
    subs = [line.split(',')[0] for line in text.splitlines() if line.strip()]
    return {"subdomains": subs}

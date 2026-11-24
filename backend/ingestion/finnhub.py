# Finnhub client. Returns the raw quote payload for one symbol.
import json
from urllib.request import urlopen

from app.env import api_key


def fetch_quote(symbol: str) -> dict:
    """Call Finnhub for the current quote."""
    token = api_key("FINNHUB_API_KEY")
    request_url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={token}"

    with urlopen(request_url, timeout=10) as response:
        return json.load(response)

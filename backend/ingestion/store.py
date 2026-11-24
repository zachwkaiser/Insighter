# Stores and reads raw Finnhub payloads in stock_quotes.
import json
from urllib.parse import quote
from urllib.request import Request, urlopen

from app.env import api_key


def latest_quote(symbol: str) -> dict | None:
    """Return the newest stored quote for a symbol, if one exists."""
    rows = _request(
        "GET",
        "stock_quotes"
        f"?symbol=eq.{quote(symbol)}"
        "&select=symbol,price,fetched_at"
        "&order=fetched_at.desc"
        "&limit=1",
    )
    if not rows:
        return None
    return rows[0]


def save_quote(symbol: str, price: float, raw: dict) -> None:
    """Save one Finnhub pull, keyed by symbol. fetched_at is set by the database."""
    _request(
        "POST",
        "stock_quotes",
        {"symbol": symbol, "price": price, "raw": raw},
    )


def _request(method: str, path: str, body: dict | None = None):
    url = api_key("SUPABASE_URL").rstrip("/") + "/rest/v1/" + path
    key = api_key("SUPABASE_SERVICE_ROLE_KEY")
    data = None if body is None else json.dumps(body).encode()

    request = Request(url, data=data, method=method)
    request.add_header("apikey", key)
    request.add_header("Authorization", f"Bearer {key}")
    request.add_header("Content-Type", "application/json")
    if body is not None:
        request.add_header("Prefer", "return=representation")

    with urlopen(request, timeout=10) as response:
        payload = response.read()
        if not payload:
            return None
        return json.loads(payload)

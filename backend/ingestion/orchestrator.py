# Decides whether to reuse a stored quote or pull a new one from Finnhub.
from datetime import UTC, datetime, timedelta

from app.models.stock import Stock
from ingestion.finnhub import fetch_quote
from ingestion.store import latest_quote, save_quote

FRESH_FOR = timedelta(seconds=30)


def load_stock(symbol: str) -> Stock:
    """Return the shared quote. Call Finnhub only when the stored copy is older than 30 seconds."""
    symbol = symbol.strip().upper()
    stored = latest_quote(symbol)

    if stored and _is_fresh(stored["fetched_at"]):
        return Stock(symbol, float(stored["price"]))

    quote = fetch_quote(symbol)
    price = float(quote["c"])
    save_quote(symbol, price, quote)
    return Stock(symbol, price)


def _is_fresh(fetched_at: str) -> bool:
    saved_at = datetime.fromisoformat(fetched_at)
    return datetime.now(UTC) - saved_at < FRESH_FOR

# Decides whether to reuse a stored quote or pull a new one from Finnhub.
from concurrent.futures import ThreadPoolExecutor
from datetime import UTC, datetime, timedelta

from app.models.stock import Stock
from ingestion.finnhub import fetch_quote
from ingestion.store import latest_quote, save_quote
from ingestion.symbols import WATCHLIST

FRESH_FOR = timedelta(seconds=30)
# Finnhub allows about 30 calls a second. Ten at a time stays under that cap.
AT_ONCE = 10


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


def load_stocks() -> list[tuple[str, Stock]]:
    """Load every watchlist quote, fetching several symbols at the same time."""
    with ThreadPoolExecutor(max_workers=AT_ONCE) as pool:
        return list(pool.map(_load_named_stock, WATCHLIST))


def _load_named_stock(entry: tuple[str, str]) -> tuple[str, Stock]:
    """Load one watchlist stock. Several of these run at the same time."""
    symbol, name = entry
    return name, load_stock(symbol)


def _is_fresh(fetched_at: str) -> bool:
    """Return whether a stored quote is still inside the 30-second window."""
    saved_at = datetime.fromisoformat(fetched_at)
    return datetime.now(UTC) - saved_at < FRESH_FOR

# Stock loading goes through ingestion so every caller shares one stored quote.
from ingestion.orchestrator import load_stock


def fetch_stock_data(symbol: str):
    """Return the shared quote for a symbol."""
    return load_stock(symbol)

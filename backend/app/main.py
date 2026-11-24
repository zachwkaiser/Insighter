# Backend entrypoint. Stock loading lives in ingestion; computation lives in analysis.

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ingestion.orchestrator import load_stock, load_stocks

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/stocks")
async def get_stocks():
    """Return a stored quote for each stock the dashboard can show."""
    return [
        {"symbol": stock.get_symbol(), "name": name, "price": stock.get_price()}
        for name, stock in load_stocks()
    ]


@app.get("/stock/{symbol}")
async def get_stock(symbol: str):
    """Return the shared quote for one symbol."""
    stock = load_stock(symbol)
    return {
        "symbol": stock.get_symbol(),
        "price": stock.get_price(),
    }
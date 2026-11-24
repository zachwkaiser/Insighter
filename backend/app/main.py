# Backend entrypoint. Stock loading lives in ingestion; computation lives in analysis.

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ingestion.orchestrator import load_stock

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/stock/{symbol}")
async def get_stock(symbol: str):
    stock = load_stock(symbol)
    return {
        "symbol": stock.get_symbol(),
        "price": stock.get_price(),
    }
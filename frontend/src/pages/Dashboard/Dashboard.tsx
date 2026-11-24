import { useEffect, useState } from "react"
import "./style.css"

type Quote = {
  symbol: string
  name: string
  price: number
}

export function Dashboard() {
  const [stocks, setStocks] = useState<Quote[]>([])
  const [symbol, setSymbol] = useState("")
  const [error, setError] = useState("")

  useEffect(() => {
    fetch("http://localhost:8000/stocks")
      .then(response => response.json())
      .then((quotes: Quote[]) => {
        setStocks(quotes)
        setSymbol(quotes[0]?.symbol ?? "")
      })
      .catch(() => setError("Could not load stocks."))
  }, [])

  const selected = stocks.find(stock => stock.symbol === symbol)

  if (error) return <p>{error}</p>
  if (stocks.length === 0) return <p>Loading stocks...</p>

  return (
    <main className="dashboard">
      <h1>Stocks</h1>
      <label htmlFor="stock">Choose a stock</label>
      <select
        id="stock"
        value={symbol}
        onChange={event => setSymbol(event.target.value)}
      >
        {stocks.map(stock => (
          <option key={stock.symbol} value={stock.symbol}>
            {stock.name} ({stock.symbol})
          </option>
        ))}
      </select>
      <p className="price">{selected?.name}: {selected?.price}</p>
    </main>
  )
}

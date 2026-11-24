import { useEffect, useState } from "react";

export function Dashboard() {
    const [price, setPrice] = useState(0);

    useEffect(() => {
        fetch("http://localhost:8000/stock/AAPL")
            .then(response => response.json())
            .then(data => {
                setPrice(data.price);
            })
            .catch(error => console.error("Error:", error));
    }, [setPrice]);

    return <p>Stock Price: {price}</p>;
}
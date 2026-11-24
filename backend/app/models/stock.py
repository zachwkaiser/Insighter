# Data shapes for stock inputs and analysis results.
class Stock:
    def __init__(self, symbol: str, price: float):
        self._symbol = symbol
        self._price = price 

    def get_symbol(self):
        return self._symbol

    def get_price(self):
        return self._price

    def set_price(self, price: float):
        self._price = price
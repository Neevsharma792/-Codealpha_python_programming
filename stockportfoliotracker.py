import requests

class StockPortfolio:
    def __init__(self, api_key):
        self.api_key = api_key
        self.portfolio = []

    def fetch_stock_data(self, symbol):
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={self.api_key}"
        try:
            response = requests.get(url)
            data = response.json()
            quote = data.get("Global Quote", {})
            return {
                "symbol": quote.get("01. symbol", symbol),
                "price": float(quote.get("05. price", 0))
            }
        except Exception as e:
            print(f"Error fetching data for {symbol}: {e}")
            return None

    def add_stock(self, symbol, quantity=1):
        stock_data = self.fetch_stock_data(symbol)
        if stock_data:
            self.portfolio.append({**stock_data, "quantity": quantity})

    def remove_stock(self, symbol):
        self.portfolio = [stock for stock in self.portfolio if stock['symbol'] != symbol]

    def get_total_value(self):
        return sum(stock['price'] * stock['quantity'] for stock in self.portfolio)

    def show_portfolio(self):
        for stock in self.portfolio:
            print(f"{stock['symbol']}: ${stock['price']} x {stock['quantity']} = ${stock['price'] * stock['quantity']:.2f}")
        print(f"Total Portfolio Value: ${self.get_total_value():.2f}")


# Example usage:
if __name__ == "__main__":
    api_key = "YOUR_API_KEY"  # Replace with your actual API key
    tracker = StockPortfolio(api_key)

    tracker.add_stock("AAPL", 5)
    tracker.add_stock("GOOGL", 2)
    tracker.show_portfolio()

    tracker.remove_stock("AAPL")
    tracker.show_portfolio()

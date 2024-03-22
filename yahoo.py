import requests
import yfinance as yf

def getPrice(symbol, start_date, end_date):
    try:
        # Create a Ticker object for the specified stock symbol
        ticker = yf.Ticker(symbol)
        
        # Fetch historical stock prices for the specified date range
        stock_data = ticker.history(start=start_date, end=end_date)
        
        # Select only the 'Open' and 'Close' columns
        open_close_prices = stock_data[['Open', 'Close']]
        
        return open_close_prices
    except Exception as e:
        print(f"Failed to fetch data from Yahoo Finance API: {e}")




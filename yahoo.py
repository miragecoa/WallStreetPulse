import requests
import yfinance as yf
import matplotlib.pyplot as plt


def getPrice(symbol, start_date, end_date):
    try:
    
        ticker = yf.Ticker(symbol)
        stock_data = ticker.history(start=start_date, end=end_date)
        open_close_prices = stock_data[['Open', 'Close']]
        
        return open_close_prices
    
    except Exception as e:
        print(f"Failed to fetch data from Yahoo Finance API: {e}")


def plot(stock_data, symbol):
    try:
        # Plotting only the 'Open' prices
        plt.figure(figsize=(10, 6))
        plt.plot(stock_data.index, stock_data['Open'], label='Open')
        plt.title(f"Historical Open Prices for {symbol}")
        plt.xlabel("Date")
        plt.ylabel("Open Price (USD)")
        plt.legend()
        plt.grid(True)
        plt.xticks(rotation=45)  
        plt.tight_layout()  
        plt.show()
        
    except Exception as e:
        print(f"Failed to plot data: {e}")
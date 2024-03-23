import yfinance as yf
import matplotlib.pyplot as plt

class StockData:
    def __init__(self, ticker):
        self.ticker = ticker
        self.data = None

    def fetch_data(self, start_date, end_date):
        self.data = yf.download(self.ticker, start=start_date, end=end_date)

    def plot_data(self):
        if self.data is not None:
            plt.figure(figsize=(14, 7))
            plt.plot(self.data['Close'])
            plt.title('Closing price of ' + self.ticker)
            plt.xlabel('Date')
            plt.ylabel('Closing Price')
            plt.grid(True)
            plt.show()
        else:
            print("No data to plot")

stock = StockData('AAPL')
stock.fetch_data('2020-01-01', '2022-12-31')
stock.plot_data()

# filename: stock_price_plot.py
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# Define the tickers and the start date for YTD
tickers = ['NVDA', 'TSLA']
start_date = '2023-01-01'  # Assuming current year is 2023

# Fetch the stock price data
data = yf.download(tickers, start=start_date)

# Normalize the data to compare percentage change from the start of the year
normalized_data = (data['Adj Close'] / data['Adj Close'].iloc[0] * 100)

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(normalized_data.index, normalized_data[tickers[0]], label='NVDA')
plt.plot(normalized_data.index, normalized_data[tickers[1]], label='TSLA')
plt.title('NVDA vs TSLA Stock Price Change YTD')
plt.xlabel('Date')
plt.ylabel('Stock Price Change (%)')
plt.legend()
plt.grid(True)
plt.show()
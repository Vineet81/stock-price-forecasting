import yfinance as yf

# Define the ticker symbol for the stock
ticker = 'AAPL'

# Download stock data from Yahoo Finance
df = yf.download(ticker, start='2020-01-01', end='2024-12-31')

# Extract only the 'Close' column
df = df[['Close']]

# Reset the index to make 'Date' a column and not the index
df.reset_index(inplace=True)

# Rename the columns to ensure 'Date' and 'Close' are clear
df = df[['Date', 'Close']]

# Save the dataframe to a CSV file
df.to_csv('data/stock_data.csv', index=False)

print("Stock data saved to 'data/stock_data.csv' with Date and Close columns.")


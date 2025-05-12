import pandas as pd

# Check the columns in your CSV file
df = pd.read_csv('data/stock_data.csv')
print(df.columns)
# Check for duplicates in the 'Date' column
print(df['Date'].duplicated().sum())  # Count duplicates
import os
print("Current working directory:", os.getcwd())


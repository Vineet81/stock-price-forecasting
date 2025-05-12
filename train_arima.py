# train_arima.py
import pandas as pd
import joblib
from statsmodels.tsa.arima.model import ARIMA

df = pd.read_csv('data/stock_data.csv', parse_dates=['Date'], index_col='Date')
series = df['Close']

model = ARIMA(series, order=(5, 1, 0))
fitted_model = model.fit()

joblib.dump(fitted_model, 'models/arima_model.pkl')


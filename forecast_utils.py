# forecast_utils.py
import pandas as pd
import numpy as np
from keras.models import load_model
import joblib
from keras.losses import MeanSquaredError
from sklearn.preprocessing import MinMaxScaler
from statsmodels.tsa.arima.model import ARIMAResults

def load_stock_data(path='data/stock_data.csv'):
    df = pd.read_csv(path, parse_dates=['Date'], index_col='Date')
    return df[['Close']]

def forecast_lstm(df, n_days=30):
    model = load_model('models/lstm_model.h5', custom_objects={'mse': MeanSquaredError()})
   # model = load_model('models/lstm_model.h5')
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(df.values)
    input_seq = scaled_data[-60:]
    predictions = []
    for _ in range(n_days):
        pred = model.predict(input_seq.reshape(1, 60, 1))[0][0]
        predictions.append(pred)
        input_seq = np.append(input_seq[1:], [[pred]], axis=0)
    return scaler.inverse_transform(np.array(predictions).reshape(-1, 1)).flatten()

def forecast_arima(df, n_days=30):
    model = joblib.load('models/arima_model.pkl')
    forecast = model.forecast(steps=n_days)
    return forecast

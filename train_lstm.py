# train_lstm.py
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler
from keras.callbacks import EarlyStopping

df = pd.read_csv('data/stock_data.csv', parse_dates=['Date'], index_col='Date')
data = df[['Close']].values

scaler = MinMaxScaler()
scaled = scaler.fit_transform(data)

X, y = [], []
for i in range(60, len(scaled)):
    X.append(scaled[i-60:i])
    y.append(scaled[i])
X, y = np.array(X), np.array(y)

model = Sequential([
    LSTM(50, return_sequences=True, input_shape=(60, 1)),
    LSTM(50),
    Dense(1)
])
model.compile(optimizer='adam', loss='mse')
model.fit(X, y, epochs=10, batch_size=32, callbacks=[EarlyStopping(patience=3)], verbose=1)

model.save('models/lstm_model.h5')

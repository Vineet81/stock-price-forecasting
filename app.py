# app.py
import streamlit as st
from forecast_utils import load_stock_data, forecast_lstm, forecast_arima
import matplotlib.pyplot as plt

st.title("📈 Stock Price Forecasting (LSTM & ARIMA)")

days = st.slider("Select number of days to forecast", 7, 90, 30)
model_type = st.radio("Choose Model", ["LSTM", "ARIMA"])
df = load_stock_data()
st.line_chart(df['Close'])

if st.button("Forecast"):
    if model_type == "LSTM":
        prediction = forecast_lstm(df, n_days=days)
    else:
        prediction = forecast_arima(df, n_days=days)

    st.subheader(f"{model_type} Forecast for {days} Days")
    st.line_chart(prediction)

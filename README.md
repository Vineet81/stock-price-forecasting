# 📈 Stock Price Forecasting App

This project predicts future stock prices using **LSTM** and **ARIMA** models, presented via a simple and interactive **Streamlit web application**. It supports **Docker** deployment and includes **CI/CD** integration via **GitHub Actions**.

---

## 🚀 Features

- 📊 Forecast stock prices using:
  - LSTM Neural Network
  - ARIMA time series model
- 📉 Visualize actual vs. predicted prices
- 🧠 Keras, TensorFlow, Scikit-learn, Statsmodels
- 🐳 Dockerized for portable and reproducible builds
- ⚙️ GitHub Actions for CI/CD deployment
- ☁️ Ready to deploy on **Streamlit Cloud**

---

## 🗂️ Project Structure

.
├── app.py
├── forecast_utils.py
├── requirements.txt
├── Dockerfile
├── data/
│ └── stock_data.csv
├── models/
│ ├── lstm_model.h5
│ └── arima_model.pkl
├── .github/
│ └── workflows/
│ └── main.yml
└── README.md


---

## 🐳 Run with Docker

```bash
# Build Docker image
docker build -t streamlit-ml-app .

# Run the container
docker run -p 8501:8501 streamlit-ml-app

Then open http://localhost:8501 in your browser.
🧪 Run Locally (without Docker)

    Optional if you're not using Docker.

pip install -r requirements.txt
streamlit run app.py

⚙️ CI/CD with GitHub Actions

GitHub Actions is configured to:

    Automatically install dependencies

    Run and deploy the Streamlit app on every push to main branch

The workflow is defined in .github/workflows/main.yml.
📁 Data & Models

    Place your stock data CSV at: data/stock_data.csv

    Trained models:

        LSTM: models/lstm_model.h5

        ARIMA: models/arima_model.pkl

    Make sure these files are committed to your repo before deploying.

📦 Requirements

    Python 3.10 or later

    Docker (optional)

    Streamlit, Pandas, NumPy, TensorFlow, Keras, Scikit-learn, Statsmodels, yfinance, etc.

📄 License

MIT License
✨ Credits

Developed by Vineet Kumar Saini
Using: Streamlit, Docker, GitHub Actions, Python ML Stack

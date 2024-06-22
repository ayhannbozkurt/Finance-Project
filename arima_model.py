import streamlit as st
from utils import get_stock_data, plot_forecast, stocks
from statsmodels.tsa.arima.model import ARIMA

def show_arima_model():
    stock_name = st.selectbox("Lütfen tahmin etmek istediğiniz hisse senedini seçin:", list(stocks.keys()))
    if stock_name:
        symbol = stocks[stock_name]
        data = get_stock_data(symbol)
        if data is not None:
            st.write("### Tahmin Sonuçları")
            steps = st.slider("Tahmin Edilmesini istediğiniz gün sayısını seçin", min_value=1, max_value=30, value=7)
            
            if st.button("Tahmin Et"):
                p, d, q = 15, 1, 5  # Sabit parametreler
                model = ARIMA(data['Close'], order=(p, d, q))
                model_fit = model.fit()
                forecast = model_fit.forecast(steps=steps)
                st.write(f"### {steps} Günlük Tahmin")
                st.write(forecast)
                plot_forecast(data, forecast.values.reshape(-1, 1), model_fit.model.endog.mean(), steps)
        else:
            st.write("Veri alınamadı. Lütfen geçerli bir sembol seçin.")

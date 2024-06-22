import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils import get_stock_data, plot_moving_average, stocks

def show_data_analysis():
    st.write("### Veri Analizi")
    stock_name = st.selectbox("Lütfen analiz etmek istediğiniz hisse senedini seçin:", list(stocks.keys()))
    if stock_name:
        symbol = stocks[stock_name]
        data = get_stock_data(symbol)
        if data is not None:
            st.write("### Yüklenen Veri")
            st.write(data.tail())
            st.write("### Veri İstatistikleri")
            st.write(data.describe())
            st.write("### Zaman Serisi Grafiği")
            st.line_chart(data['Close'])
            
            st.write("### Hareketli Ortalama Hesaplama")
            window = st.slider("Hareketli Ortalama Süresi (Gün)", min_value=1, max_value=50, value=20)
            plot_moving_average(data, window)
        else:
            st.write("Veri alınamadı. Lütfen geçerli bir sembol seçin.")

import streamlit as st
from data_analysis import show_data_analysis
from arima_model import show_arima_model
from reporting import show_reporting
from scraping import get_news, color_label

st.set_page_config(layout="wide")  # Sayfa genişliğini tam genişlik olarak ayarlar

st.title("Finansal Veri Analizi ve Tahminleme Uygulaması")

st.sidebar.header("Menü")
menu = st.sidebar.radio(
    "Secenekler",
    ["Ana Sayfa", "Veri Analizi", "Model Egitimi ve Tahminleme", "Raporlama", "Sentiment Analysis"]
)

if menu == "Ana Sayfa":
    st.write("""
    ### Hoşgeldiniz!
    Bu uygulama finansal veri analizi ve tahminleme işlemleri için geliştirilmiştir.
    Sol taraftaki menüden istediğiniz işlemi seçerek devam edebilirsiniz.
    """)

elif menu == "Veri Analizi":
    show_data_analysis()

elif menu == "Model Egitimi ve Tahminleme":
    show_arima_model()

elif menu == "Raporlama":
    show_reporting()

elif menu == "Sentiment Analysis":
    get_news()
import streamlit as st
from data_analysis import show_data_analysis
from arima_model import show_arima_model
from reporting import show_reporting
from scraping import get_news, color_label
import os
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

# API anahtarını al
global api_key
api_key = os.getenv('api_key')

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
    df = get_news()
    st.write("Finansal Haberler ve Duygu Analizi")
    
    # Tabloyu tam genişlikte göstermek için streamlit style kullanımı
    st.markdown("""
        <style>
        .reportview-container .main .block-container{
            padding: 0;
        }
        </style>
        """, unsafe_allow_html=True)
    
    # DataFrame'i tam genişlikte göster
    st.dataframe(df.style.applymap(color_label, subset=['Label']), width=1500, height=800)

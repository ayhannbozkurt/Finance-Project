# Financial-Analysis-Project

Bu proje, finansal veri analizi ve tahminleme işlemleri için geliştirilmiş bir uygulamadır. Kullanıcılar, hisse senedi verilerini analiz edebilir, tahminler yapabilir ve bu verilere dayalı karar önerileri alabilirler. Uygulama, Streamlit arayüzü kullanılarak geliştirilmiştir ve OpenAI'nın GPT-3.5 modelini kullanarak karar önerileri sunar.


Proje Mantığı ve Yapılanlar
1. Veri Analizi (data_analysis.py)
Kullanıcılar, hisse senedi verilerini analiz edebilirler. Kullanıcı, analiz yapmak istediği hisse senedini seçer ve uygulama, bu hisse senedinin verilerini gösterir. Verilerin özet istatistiklerini ve zaman serisi grafiğini içerir. Kullanıcı ayrıca hareketli ortalama hesaplamalarını da yapabilir.

2. ARIMA Modeli ile Tahmin (arima_model.py)
Kullanıcılar, ARIMA modeli kullanarak hisse senedi fiyatlarının tahminlerini yapabilirler. ARIMA modelinin parametreleri olan p, d ve q sabit olarak belirlenmiştir. Kullanıcı, tahmin adımlarını seçerek gelecekteki fiyat tahminlerini görebilir.

3. Karar Önerileri ve GPT Entegrasyonu (reporting.py)
Bu modülde, kullanıcıların analiz sonuçlarına dayalı karar önerileri alması sağlanır. OpenAI GPT-3.5 API'si kullanılarak, analiz sonuçlarına göre hisse senedinin alınması veya satılması önerileri sunulur. Kullanıcı, analiz yapmak istediği hisse senedini seçer, veri özetini ve analiz sonuçlarını görür ve ardından GPT-3.5 API'si tarafından sağlanan karar önerilerini alır.

4. Yardımcı Fonksiyonlar (utils.py)
Bu dosya, veri çekme ve görselleştirme işlemlerini içeren yardımcı fonksiyonları içerir. Hisse senedi verilerini almak ve çeşitli grafikler oluşturmak için kullanılır.

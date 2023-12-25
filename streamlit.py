import streamlit as st
import pandas as pd
import datetime
import plotly.express as px
import pickle
from statsmodels.tsa.statespace.sarimax import SARIMAXResults
import joblib



st.set_page_config(layout = "wide")
@st.cache_data
def get_data():
    df = pd.read_csv("output.csv")
    return df
def get_model():
    model = joblib.load(r"sarima_final_model.pkl")
    return model


st.header("🔌💡:blue[Tüketilecek Elektrik Tahmini]🧑‍🔧")
tab_home, tab_vis,tab_model = st.tabs(["Anasayfa","Grafikler","Model"])

#TAB HOME#

column_hans, column_dataset = tab_home.columns(2,gap = "large")


column_hans.subheader(":gray[Elektrik Tüketimini Tahmin Etmenin Faydaları]")
column_hans.markdown("""
* **Enerji Üretimi ve Tedarik Planlaması:** Elektrik tüketimini doğru bir şekilde tahmin etmek, enerji üreticilerinin ve dağıtıcılarının ihtiyaç duyulan enerjiyi etkin bir şekilde üretmeleri ve dağıtmaları için hayati öneme sahiptir. Bu, hem aşırı üretimi hem de enerji eksikliğini önlemeye yardımcı olur.

* **Altyapı Yatırımları:** Gelecekteki elektrik talebini tahmin etmek, altyapı yatırımlarını planlamada kritik bir rol oynar. Enerji şirketleri, enerji ihtiyacını karşılamak için hangi bölgelere yeni tesisler veya güç hatları kurulması gerektiğine karar verirken bu bilgileri kullanır.

* **Fiyatlandırma Stratejileri:** Elektrik tüketim tahminleri, fiyatlandırma stratejilerini belirlemeye yardımcı olur. Örneğin, talebin yüksek olduğu zamanlarda elektrik fiyatları artabilirken, talebin düşük olduğu zamanlarda daha uygun fiyatlar sunulabilir.

* **Enerji Verimliliği:** Tüketim tahminleri, enerji verimliliği çabalarını şekillendirmede önemlidir. Örneğin, tüketimin yoğun olduğu saatlerde enerji tasarrufu yapmak veya enerji verimliliği önlemlerini uygulamak, genel tüketimi düşürebilir.

* **Yenilenebilir Enerji Entegrasyonu:** Yenilenebilir enerji kaynaklarının, özellikle güneş ve rüzgar enerjisinin doğası gereği değişken olması, doğru tüketim tahminlerinin önemini artırır. Enerji şirketleri, yenilenebilir enerji üretimini ve geleneksel enerji kaynaklarını daha iyi dengeler.

* **Acil Durum Planlaması:** Aşırı hava olayları veya diğer acil durumlar sırasında enerji talebinin doğru bir şekilde tahmin edilmesi, bu tür durumlara hazırlanmak için önemlidir. Örneğin, büyük bir fırtına öncesinde artan talebi karşılamak için ek kaynaklar mobilize edilebilir.

* **Karar Verme ve Politika Geliştirme:** Hükümetler ve düzenleyici kurumlar, enerji politikalarını ve düzenlemelerini, gelecekteki elektrik tüketim tahminlerine dayanarak şekillendirir.

* **Tüketiciler için Bilgi:** Son olarak, tüketiciler için de tüketim tahminleri önemlidir. Özellikle akıllı şebeke teknolojilerinin artmasıyla birlikte, tüketiciler kendi enerji kullanımlarını daha etkin bir şekilde yönetebilir ve enerji maliyetlerini düşürebilirler.
""")



column_dataset.subheader("Veri Seti Hakkında")
column_dataset.markdown("Almanya'nın 2015-2020 yılları arasında 5 yıllık güç tüketim verisi vardır.Bu projede zaman serileriyle 2020 yılı aylarında ne kadar tüketim olabileceği tahminini yapacağız")
#  Local URL: http://localhost:8501
#Network URL: http://192.168.1.36:8501
df = get_data()
column_dataset.dataframe(df,width = 500)

#TAB VIS
##grafik

tab_vis.subheader("Almanya'da Geçmiş Yıllarda Aylara Göre Güç Tüketimi")

#tab_vis.multiselect("label = Tarih seçiniz", option )
# String tarihleri datetime'a dönüştürme
df["date"] = pd.to_datetime(df["date"])

# Tarihleri yıllarına göre gruplandırma
yillar = set(tarih.year for tarih in df["date"])  # Benzersiz yılları al

# Streamlit uygulaması
tab_vis.title('Yıla Göre Tarih Seçimi')

# Multiselect widget'ını yıllarla kullanma
secilen_yillar = tab_vis.multiselect('Yıl(ları) Seçiniz:', sorted(yillar))

# Seçilen yıllara ait tarihleri filtrele
secilen_tarihler = [tarih for tarih in df["date"] if tarih.year in secilen_yillar]

filtered_df = df[df.date.isin(secilen_tarihler)]
# 'date' sütununu kullanarak 'year' sütunu oluşturma
filtered_df['year'] = filtered_df['date'].dt.year

fig = px.line(
    filtered_df,
    x = "date",
    y = "load",
    color = "year"
)
tab_vis.plotly_chart(fig, use_container_width=True)

## grafik3

tab_vis.subheader("Almanya'da Geçmiş Yıllarda Aylara Göre Güç Tüketimi Değişimi")

fig_2 = px.scatter(
    filtered_df,
    x="date",
    y="load",
    color="year",
    animation_frame="year",  # Yıl bazında animasyon,
    hover_name="date",
    size_max=60
)

fig_2.add_hline(y=50, line_dash="dash", line_color="black")
tab_vis.plotly_chart(fig_2, user_container_width=True)

# TAB MODEL
import pandas as pd

# Modeli yükle
model = get_model()

# Tarih seçimi
date = tab_model.date_input("Yıl Giriniz",
                            value=pd.to_datetime("2020-01-01"),
                            min_value=pd.to_datetime("2020-01-01"),
                            max_value=pd.to_datetime("2023-01-01"))

# Seçilen tarihi al
selected_date = date

# Tahmin yapma butonu
if tab_model.button("Tahmin et!"):
    # Modelin beklediği formatta veri gönder
    prediction = model.predict(selected_date)

    # Tahmin değerini sayıya dönüştür ve sadece sayısal değeri göster
    prediction_value = prediction.iloc[0]
    if isinstance(prediction_value, pd.Series):
        prediction_value = prediction_value.iloc[0]  # Eğer Seri ise ilk elemanı al
    tab_model.success(f"Tahmin edilen güç tüketimi miktarı: {prediction_value}")
    tab_model.balloons()
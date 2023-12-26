# streamlit-timeseries
Almanya'nın 2015-2020 yılları arasında 5 yıllık güç tüketim verisi vardır.Bu projede zaman serileriyle 2021 yılı aylarında ne kadar tüketim olabileceği tahminini yapacağız
1. Veri Toplama:​
Tarihsel Elektrik Tüketim Verileri: Almanya'nın geçmiş yıllara ait saatlik, günlük elektrik tüketim verileri.​
Bu verilerle aylık elektrik tüketimini gösterecek şekilde düzenleyerek kullandım.
2. Veri Ön İşleme:​
Veri Temizleme: Eksik veya hatalı verilerin düzeltilmesi.​
Sezonsallığın ve Trendlerin Belirlenmesi: Yıl içindeki ve yıllar arası tüketim trendlerinin ve mevsimsel dalgalanmaların analizi.​
3. Model Seçimi ve Geliştirme:​
Zaman Serisi Modelleri: SARIMA (Mevsimsel ARIMA), modelini kullandım. Bu model trend ve| veya mevsimsellik içeren tek değişkenli serilerde kullanılabilir.
4. Model Eğitimi ve Doğrulama:​
Eğitim ve Test Setlerinin Ayrılması: Verilerin bir kısmı modeli eğitmek için, diğer kısmı modelin doğruluğunu test etmek için ayırdım.
Modelin Performansının Değerlendirilmesi:MAE (Ortalama Mutlak Hata) hata ölçütünü kullandım.
5. Tahminlerin Yapılması:​
Kurulan modelde bulunmayan 2020'nin 8 aylık elektrik tüketimini tahmin ettim.

![Alt text](image-4.png)
![Alt text](<Ekran Görüntüsü (183)-1.png>)
![Alt text](<indir (2).png>)
![Alt text](<indir (1).png>)
![Alt text](indir.png)
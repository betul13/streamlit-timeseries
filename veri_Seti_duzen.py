import pandas as pd
df = pd.read_csv(r"C:\Users\bett0\Desktop\datasets\de.csv")

df.dropna(inplace = True)
df.isnull().sum()


df["start"] = pd.to_datetime(df["start"])
df["end"] = pd.to_datetime(df["end"])



df["date"] = df['end'].apply(lambda x: x.strftime('%Y-%m-%d')) #sadece tarih kısmını alır
df = df.drop(["start","end"], axis = 1) #bu verilere gerek kalmadı.Aylık harcanan güç miktarı yeterli olacaktır.


df["date"] = pd.to_datetime(df["date"])

df = df.groupby("date").sum().reset_index()

df = df[df['date'].dt.year != 2020]
df["date"] = df['date'].dt.to_period('M')

monthly_total_load = df.groupby('date')['load'].sum().reset_index()
df = monthly_total_load

df['date'] = df['date'].dt.to_timestamp()
# 'date' sütununu indeks olarak ayarla

df.to_csv('output.csv', index=False)
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("clean_data.csv")

# Pastikan kolom tanggal dalam format datetime
df['tanggal'] = pd.to_datetime(df['tanggal'])

# Ekstrak tahun dan bulan
df['tahun'] = df['tanggal'].dt.year
df['bulan'] = df['tanggal'].dt.month

# Sidebar filter
st.title("Tren Bulanan PM2.5 dan PM10 per Stasiun")
st.sidebar.header("Filter Data")

stasiun_list = df['stasiun'].unique()
selected_stasiun = st.sidebar.selectbox("Pilih Stasiun", stasiun_list)

# Filter data berdasarkan stasiun
df_filtered = df[df['stasiun'] == selected_stasiun]

# Hitung rata-rata bulanan untuk PM2.5 dan PM10
monthly_avg = df_filtered.groupby(['tahun', 'bulan'])[['pm_duakomalima', 'pm_sepuluh']].mean().reset_index()

# Gabungkan tahun dan bulan menjadi satu kolom untuk x-axis
# Pastikan tahun dan bulan bertipe integer
monthly_avg['tahun'] = monthly_avg['tahun'].astype(int)
monthly_avg['bulan'] = monthly_avg['bulan'].astype(int)

# Gabungkan ke datetime
monthly_avg['periode'] = pd.to_datetime(dict(year=monthly_avg['tahun'], month=monthly_avg['bulan'], day=1))

# Plot
plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_avg, x='periode', y='pm_duakomalima', marker='o', label='PM2.5')
sns.lineplot(data=monthly_avg, x='periode', y='pm_sepuluh', marker='o', label='PM10')

# Tambahkan nilai pada titik-titik garis
for i in range(len(monthly_avg)):
    plt.text(monthly_avg['periode'][i], monthly_avg['pm_duakomalima'][i]+0.5,
             f"{monthly_avg['pm_duakomalima'][i]:.1f}", ha='center', color='blue')
    plt.text(monthly_avg['periode'][i], monthly_avg['pm_sepuluh'][i]+0.5,
             f"{monthly_avg['pm_sepuluh'][i]:.1f}", ha='center', color='orange')

plt.title(f"Tren Bulanan PM2.5 dan PM10 di Stasiun {selected_stasiun}")
plt.xlabel("Periode (Bulan)")
plt.ylabel("Konsentrasi (µg/m³)")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(plt)

# Penjelasan matriks
st.subheader("Penjelasan Matriks")
st.markdown("""
- **PM2.5 (pm_duakomalima)**: Partikulat udara berdiameter kurang dari 2.5 mikron, dapat menembus jauh ke dalam saluran pernapasan.
- **PM10 (pm_sepuluh)**: Partikulat udara berdiameter kurang dari 10 mikron, berasal dari debu jalanan, asap kendaraan, dll.
- Nilai yang ditampilkan adalah **rata-rata bulanan** berdasarkan data harian.
- Grafik menunjukkan tren musiman dan perbandingan antara PM2.5 dan PM10 di stasiun terpilih.
""")

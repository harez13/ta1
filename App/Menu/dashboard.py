import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('clean_data.csv')

# Pastikan kolom tanggal dalam datetime
df['tanggal'] = pd.to_datetime(df['tanggal'])

# Tambahkan kolom Tahun dan Bulan
df['Tahun'] = df['tanggal'].dt.year
df['Bulan'] = df['tanggal'].dt.month

# Sidebar filter
st.sidebar.title("Filter Data")
stasiun_list = df['stasiun'].unique()
stasiun = st.sidebar.selectbox("Pilih Stasiun", stasiun_list)

bulan_min = int(df['Bulan'].min())
bulan_max = int(df['Bulan'].max())
bulan_range = st.sidebar.slider("Pilih Rentang Bulan", bulan_min, bulan_max, (1, 12))

# Filter data berdasarkan input pengguna
filtered_df = df[
    (df['stasiun'] == stasiun) &
    (df['Bulan'] >= bulan_range[0]) &
    (df['Bulan'] <= bulan_range[1])
]

# Group dan agregasi data
agg_df = filtered_df.groupby(['Tahun', 'Bulan'])[['pm_duakomalima', 'pm_sepuluh']].mean().reset_index()

# Plot
st.title("Tren Bulanan pm_duakomalima dan pm_sepuluh")
st.write(f"Stasiun: **{stasiun}** | Bulan: **{bulan_range[0]} - {bulan_range[1]}**")

fig, ax = plt.subplots(figsize=(10, 5))
for tahun in agg_df['Tahun'].unique():
    tahun_data = agg_df[agg_df['Tahun'] == tahun]
    ax.plot(tahun_data['Bulan'], tahun_data['pm_duakomalima'], marker='o', label=f'pm_duakomalima - {tahun}')
    ax.plot(tahun_data['Bulan'], tahun_data['pm_sepuluh'], marker='s', linestyle='--', label=f'pm_sepuluh - {tahun}')

ax.set_title("Rata-rata pm_duakomalima dan pm_sepuluh per Bulan")
ax.set_xlabel("Bulan")
ax.set_ylabel("Konsentrasi (µg/m³)")
ax.legend()
ax.grid(True)
st.pyplot(fig)
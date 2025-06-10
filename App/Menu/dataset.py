import streamlit as st
import pandas as pd

# Judul Aplikasi
st.title("Tampilan Dataset Indeks Standar Pencemar Udara (ISPU)")

# Membaca dataset
df = pd.read_csv("clean_data.csv")

# Menghapus kolom pertama (biasanya index atau ID)
df = df.iloc[:, 1:]

# Menampilkan dataset
st.markdown("### Dataset")
st.dataframe(df)

# Menampilkan keterangan
st.markdown("### Keterangan Komponen Dataset:")
st.markdown("""
- **periode_data**: Penjelasan Periode Data 1 Bulan Sekali  
- **bulan**: Bulan pengambilan data ISPU  
- **tanggal**: Tanggal pengambilan data ISPU  
- **stasiun**: Lokasi penempatan alat pemantauan udara  
- **pm_sepuluh**: Nilai ISPU untuk PM10 (partikulat <10 mikron)  
- **pm_duakomalima**: Nilai ISPU untuk PM2.5 (partikulat <2.5 mikron)  
- **sulfur_dioksida**: Nilai ISPU untuk SO2  
- **karbon_monoksida**: Nilai ISPU untuk CO  
- **ozon**: Nilai ISPU untuk O3  
- **nitrogen_dioksida**: Nilai ISPU untuk NO2  
- **max**: Nilai ISPU tertinggi dari parameter-parameter yang dipantau  
- **parameter_pencemar_kritis**: Parameter dengan ISPU tertinggi pada tanggal dan stasiun tertentu  
- **kategori**: Kategori hasil pengukuran ISPU  
""")


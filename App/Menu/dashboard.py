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
st.subheader("Penjelasan PM2.5 dan PM10")

# Buat dua kolom
col1, col2 = st.columns(2)

with col1:
    st.markdown("### PM2.5")
    st.markdown("_Partikel halus (≤ 2.5 µm)_")
    st.markdown("""
**Apa itu PM2.5?**  
PM2.5 merupakan partikel yang mengambang di udara dengan ukuran diameter 2,5 mikrometer atau kurang. Ukurannya sangat kecil sehingga dapat diserap ke dalam aliran darah saat bernapas dan menimbulkan ancaman kesehatan besar.

**Dari mana ia datang?**
- Pembakaran bahan bakar (misalnya di pembangkit listrik)
- Asap dan jelaga dari kebakaran hutan atau limbah
- Emisi kendaraan bermotor
- Proses industri dan reaksi kimia

**Bagaimana memengaruhi kesehatan?**
***Efek jangka pendek***:
- Iritasi pada mata, tenggorokan, dan hidung
- Detak jantung tidak teratur
- Batuk, nyeri dada, sakit tenggorokan, sesak napas
- Serangan asma
                
***Efek jangka pendek***:
- Penyakit pernafasan seperti bronkitis, asma, emfisema
- Kerusakan jaringan paru-paru
- Kanker
- Serangan jantung
- Stroke
- Kematian dini
""")

with col2:
    st.markdown("### PM10")
    st.markdown("_Partikel kasar (≤ 10 µm)_")
    st.markdown("""
**Apa itu PM10?**  
Partikel dengan ukuran hingga 10 mikrometer (termasuk debu, jelaga, garam, logam, dll). PM10 lebih besar dan kasar dibandingkan PM2.5.

**Dari mana ia datang?**
- Debu dari konstruksi dan pertanian
- Debu jalanan yang tertiup angin
- Asap dari kebakaran atau pembakaran
- Gas dan partikel dari kendaraan

**Bagaimana memengaruhi kesehatan?**
***Efek jangka pendek***:
- Kesulitan bernapas
- Sakit dada
- Ketidaknyamanan pernapasan
- Sakit tenggorokan
- Hidung tersumbat
                
***Efek jangka pendek***:
- Kerusakan jaringan paru-paru
- Kanker
- Asma
- Kematian dini
                
Sumber : [IQAir]('https://www.iqair.com/id/support/knowledge-base')
""")


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

# Sidebar navigasi
option = st.sidebar.selectbox(
    "Pilih Visualisasi:",
    (
        "1. Korelasi Antar Parameter Pencemar",
        "2. Rata-Rata Bulanan Parameter Pencemar",
        "3. Distribusi Kategori Kualitas Udara per Stasiun",
        "4. Frekuensi Parameter Pencemar Kritis per Stasiun",
        "5. Tren Harian PM2.5 per Stasiun"
    )
)

if option == "1. Korelasi Antar Parameter Pencemar":
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
                    
    ***Efek jangka panjang***:
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
                    
    ***Efek jangka panjang***:
    - Kerusakan jaringan paru-paru
    - Kanker
    - Asma
    - Kematian dini
                    
    Sumber : [IQAir]('https://www.iqair.com/id/support/knowledge-base')
    """)

# --- Visualisasi 2 ---
elif option == "2. Rata-Rata Bulanan Parameter Pencemar":
    # Sidebar: Filter stasiun
st.title("Tren Bulanan Kategori Kualitas Udara")
st.sidebar.header("Filter")
stasiun_list = df['stasiun'].unique()
selected_stasiun = st.sidebar.selectbox("Pilih Stasiun", stasiun_list)

# Filter data
df_filtered = df[df['stasiun'] == selected_stasiun]

# Hitung jumlah kategori per bulan
kategori_bulanan = df_filtered.groupby(['tahun', 'bulan', 'kategori']).size().reset_index(name='jumlah')
kategori_bulanan['periode'] = pd.to_datetime(dict(year=kategori_bulanan['tahun'], 
                                                  month=kategori_bulanan['bulan'], day=1))

# Plot
plt.figure(figsize=(12, 6))
sns.set(style="whitegrid")

for kategori in kategori_bulanan['kategori'].unique():
    df_kat = kategori_bulanan[kategori_bulanan['kategori'] == kategori]
    sns.lineplot(data=df_kat, x='periode', y='jumlah', marker='o', label=kategori)
    for i in range(len(df_kat)):
        plt.text(df_kat['periode'].iloc[i], df_kat['jumlah'].iloc[i] + 0.3,
                 str(df_kat['jumlah'].iloc[i]), ha='center', fontsize=8)

plt.title(f"Tren Bulanan Kategori Kualitas Udara - Stasiun {selected_stasiun}")
plt.xlabel("Periode (Bulan)")
plt.ylabel("Jumlah Hari per Kategori")
plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(plt)

# Penjelasan kategori kualitas udara
st.subheader("Penjelasan Kategori Kualitas Udara")

st.markdown("""
Berikut ini adalah kategori kualitas udara berdasarkan konsentrasi partikulat (misalnya PM2.5 atau PM10):

| Kategori       | Deskripsi                                                                 |
|----------------|---------------------------------------------------------------------------|
| **Baik**       | Tidak berdampak pada kesehatan.                                           |
| **Sedang**     | Tidak berpengaruh bagi masyarakat umum, tetapi berdampak untuk kelompok sensitif. |
| **Tidak Sehat**| Berdampak pada kelompok sensitif dan bisa berdampak ringan pada masyarakat umum. |
| **Sangat Tidak Sehat** | Berdampak serius pada kelompok sensitif dan masyarakat umum.      |
| **Berbahaya**  | Kondisi darurat kesehatan. Semua orang bisa terdampak.                   |

Kategori di atas bisa disesuaikan dengan sistem seperti **ISPU** (Indeks Standar Pencemar Udara) Indonesia.
""")
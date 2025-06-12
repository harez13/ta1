import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import plotly.express as px

# Load data
df = pd.read_csv("clean_data.csv")

# Pastikan kolom tanggal dalam format datetime
df['tanggal'] = pd.to_datetime(df['tanggal'])


# Ekstrak tahun dan bulan
df['tahun'] = df['tanggal'].dt.year
df['bulan'] = df['tanggal'].dt.month
df['nama_bulan'] = df['tanggal'].dt.strftime('%B')

# Sidebar navigasi
option = st.sidebar.selectbox(
    "Pilih Visualisasi:",
    (
        "1. Tren Bulanan PM2.5 dan PM10 per Stasiun",
        "2. Tren Bulanan Kategori Kualitas Udara",
        "3. Time Series Matrix per Stasiun",
        "4. Frekuensi Parameter Pencemar Kritis per Stasiun",
        "5. Tren Harian PM2.5 per Stasiun"
    )
)

if option == "1. Tren Bulanan PM2.5 dan PM10 per Stasiun":
    # Sidebar filter
    st.title("Tren Bulanan PM2.5 dan PM10 per Stasiun")

    stasiun_list = df['stasiun'].unique()
    selected_stasiun = st.selectbox("Pilih Stasiun", stasiun_list)

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
elif option == "2. Tren Bulanan Kategori Kualitas Udara":
    # Sidebar: Filter stasiun
    st.title("Tren Bulanan Kategori Kualitas Udara")

    stasiun_list = df['stasiun'].unique()
    selected_stasiun = st.selectbox("Pilih Stasiun", stasiun_list)

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

# --- Visualisasi 3 ---
elif option == "3. Time Series Matrix per Stasiun":
    

   

    # Plot per stasiun
    st.title("Time Series Matrix per Stasiun")

    parameter = st.selectbox(
        "Pilih Parameter Pencemar",
        ["pm_sepuluh", "pm_duakomalima", "sulfur_dioksida", "karbon_monoksida", "ozon", "nitrogen_dioksida"]
    )

    # Pilih stasiun
    stations = st.multiselect(
        "Pilih Stasiun Pemantau",
        options=df["stasiun"].unique(),
        default=df["stasiun"].unique()
    )

     # Filter data
    filtered_df = df[df["stasiun"].isin(stations)].copy()
    
    fig, axes = plt.subplots(nrows=len(stations), ncols=1, figsize=(12, 4 * len(stations)), sharex=True)

    if len(stations) == 1:
        axes = [axes]  # Agar iterable

    for ax, station in zip(axes, stations):
        station_data = filtered_df[filtered_df["stasiun"] == station]
        sns.lineplot(data=station_data, x="tanggal", y=parameter, ax=ax)
        ax.set_title(f"{station}", fontsize=14)
        ax.set_ylabel(parameter)
        ax.grid(True)

    plt.xlabel("Tanggal")
    plt.tight_layout()
    st.pyplot(fig)

    st.markdown("""
    Visualisasi ini menampilkan **grafik deret waktu** (time series) untuk parameter pencemar udara dari berbagai **stasiun pemantauan di DKI Jakarta**.
    """)

# --- Visualisasi 4 ---
elif option == "4. Frekuensi Parameter Pencemar Kritis per Stasiun":
    
    # Konversi kategori ke nilai numerik
    kategori_mapping = {
        'BAIK': 1,
        'SEDANG': 2,
        'TIDAK SEHAT': 3,
        'SANGAT TIDAK SEHAT': 4,
        'BERBAHAYA': 5
    }
    df['kategori_nilai'] = df['kategori'].map(kategori_mapping)

    # Pilih kolom yang akan dihitung korelasinya
    pollutant_cols = ['pm_sepuluh', 'pm_duakomalima', 'sulfur_dioksida',
                    'karbon_monoksida', 'ozon', 'nitrogen_dioksida', 'kategori_nilai']

    # Korelasi antara parameter pencemar dan kualitas udara
    corr_matrix = df[pollutant_cols].corr()[['kategori_nilai']].drop('kategori_nilai')

    # Buat heatmap korelasi
    st.title("🌫️ Korelasi Parameter Pencemar terhadap Kualitas Udara")

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5, ax=ax)
    ax.set_title("Korelasi Parameter Pencemar vs Kategori Kualitas Udara")
    st.pyplot(fig)

    # Penjelasan
    st.markdown("""
    ---

    ### ℹ️ Penjelasan Visualisasi:

    - Heatmap ini menunjukkan **tingkat hubungan antara setiap parameter pencemar** dan **tingkat kategori kualitas udara** yang telah dinyatakan dalam bentuk angka (1–5).
    - **Semakin tinggi nilai korelasi (positif), semakin besar kontribusi parameter tersebut terhadap memburuknya kualitas udara**.
    """)

    
# --- Visualisasi 5 ---
elif option == "5. Tren Harian PM2.5 per Stasiun":
    # Sidebar filter
    st.sidebar.header("🧭 Filter Bubble Chart")
    param_kolom = st.sidebar.selectbox("Pilih parameter pencemar (nilai aktual):", df.columns[5:], help="Pilih kolom nilai numerik, seperti PM2.5 atau lainnya.")

    # Pilih rentang tanggal
    min_date = df['tanggal'].min()
    max_date = df['tanggal'].max()
    rentang_tanggal = st.sidebar.date_input("Rentang tanggal:", [min_date, max_date])

    # Filter data
    df_filtered = df[(df['tanggal'] >= pd.to_datetime(rentang_tanggal[0])) & (df['tanggal'] <= pd.to_datetime(rentang_tanggal[1]))]

    # Bubble Chart
    st.title("🫧 Bubble Chart: Tanggal vs Stasiun")
    st.subheader(f"Parameter: {param_kolom} | Periode: {rentang_tanggal[0]} s.d. {rentang_tanggal[1]}")

    fig = px.scatter(
        df_filtered,
        x='tanggal',
        y='stasiun',
        size=param_kolom,
        color=param_kolom,
        hover_data=['tanggal', 'stasiun', param_kolom],
        size_max=40,
        color_continuous_scale='YlOrRd',
        title="Visualisasi Intensitas Pencemaran Harian per Stasiun"
    )

    fig.update_layout(
        xaxis_title='Tanggal',
        yaxis_title='Stasiun Pemantauan',
        legend_title='Nilai Pencemar',
        height=600
    )

    st.plotly_chart(fig, use_container_width=True)

    # Penjelasan visualisasi
    st.markdown("""
    ---

    ### 🧠 Penjelasan Bubble Chart

    - **Sumbu X:** Tanggal pengukuran.
    - **Sumbu Y:** Nama stasiun pemantauan.
    - **Ukuran gelembung:** Besarnya nilai parameter pencemar (misalnya PM2.5, PM10, CO).
    - **Warna:** Mewakili tingkat pencemaran (semakin merah, semakin tinggi nilainya).

    ---

    ### 📌 Fungsi Visualisasi:
    - Mengidentifikasi **puncak pencemaran** di hari dan stasiun tertentu.
    - Melihat **tren lonjakan** atau kejadian **anomali lokal** (misalnya satu stasiun ekstrem di hari tertentu).
    - Membandingkan **aktivitas pencemar** antar stasiun dalam satu waktu.

    ---

    ### 🎯 Insight yang Bisa Diperoleh:
    - Titik-titik besar pada satu tanggal = kemungkinan **kejadian ekstrem lokal**.
    - Jika semua stasiun memiliki gelembung besar di hari yang sama → indikasi **pencemaran regional**.
    - Pola-pola berulang mingguan/bulanan bisa dianalisis lebih lanjut.

    """)
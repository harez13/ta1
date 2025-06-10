import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px



# Load data
df = pd.read_csv("clean_data.csv")
df['tanggal'] = pd.to_datetime(df['tanggal'], dayfirst=True, errors='coerce')
df['tahun'] = df['tanggal'].dt.year
df['bulan'] = df['tanggal'].dt.month

# Judul utama
st.title("📊 Dashboard Kualitas Udara Jakarta 2024")

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

# List parameter pencemar
pollutants = ['pm_sepuluh', 'pm_duakomalima', 'sulfur_dioksida',
              'karbon_monoksida', 'ozon', 'nitrogen_dioksida']

# --- Visualisasi 1 ---
if option == "1. Korelasi Antar Parameter Pencemar":
    # Mapping dari 'parameter_pencemar_kritis' ke kolom numerik
    param_map = {
        "PM10": "pm_sepuluh",
        "PM25": "pm_duakomalima",
        "SO2": "sulfur_dioksida",
        "CO": "karbon_monoksida",
        "O3": "ozon",
        "NO2": "nitrogen_dioksida"
    }

    st.title("Tren Bulanan Parameter Pencemar Kritis per Tahun")
    st.markdown("""
    Pilih **parameter pencemar kritis** dan **stasiun pemantauan** untuk melihat bagaimana polutan berubah tiap bulan dalam satuan tahunan.
    """)

    # Dropdowns untuk filter
    param_kritis_list = df['parameter_pencemar_kritis'].unique().tolist()
    selected_param = st.selectbox("Pilih Parameter Pencemar Kritis:", param_kritis_list)
    selected_stasiun = st.selectbox("Pilih Stasiun:", df['stasiun'].unique())

    # Kolom parameter numerik
    param_col = param_map.get(selected_param, None)

    if param_col:
        # Filter berdasarkan pilihan
        df_filtered = df[(df['parameter_pencemar_kritis'] == selected_param) & (df['stasiun'] == selected_stasiun)]

        # Agregasi rata-rata per bulan-tahun
        monthly_trend = df_filtered.groupby(['tahun', 'bulan'])[param_col].mean().reset_index()

        # Visualisasi dengan line plot
        fig = px.line(
            monthly_trend,
            x="bulan",
            y=param_col,
            color="tahun",
            markers=True,
            title=f"Tren Bulanan {selected_param} di {selected_stasiun}",
            labels={"bulan": "Bulan", param_col: "Konsentrasi Rata-rata", "tahun": "Tahun"}
        )
        fig.update_xaxes(dtick=1, title='Bulan (1-12)')
        st.plotly_chart(fig)
    else:
        st.warning("Parameter yang dipilih tidak memiliki data numerik yang cocok.")
# --- Visualisasi 2 ---
# elif option == "2. Rata-Rata Bulanan Parameter Pencemar":
#     st.subheader("📆 Rata-Rata Bulanan Parameter Pencemar")
#     pollutant_month = df.groupby("bulan")[pollutants].mean().T
#     fig, ax = plt.subplots(figsize=(10, 6))
#     sns.heatmap(pollutant_month, annot=True, fmt=".1f", cmap="YlOrRd", ax=ax)
#     ax.set_xlabel("Bulan")
#     ax.set_ylabel("Parameter")
#     st.pyplot(fig)

# # --- Visualisasi 3 ---
# elif option == "3. Distribusi Kategori Kualitas Udara per Stasiun":
#     st.subheader("🏙️ Distribusi Kategori Kualitas Udara per Stasiun")
#     kategori_matrix = df.groupby(["stasiun", "kategori"]).size().unstack(fill_value=0)
#     fig, ax = plt.subplots(figsize=(10, 6))
#     sns.heatmap(kategori_matrix, annot=True, cmap="Blues", fmt="d", ax=ax)
#     st.pyplot(fig)

# # --- Visualisasi 4 ---
# elif option == "4. Frekuensi Parameter Pencemar Kritis per Stasiun":
#     st.subheader("⚠️ Frekuensi Parameter Pencemar Kritis per Stasiun")
#     critical_matrix = df.groupby(["stasiun", "parameter_pencemar_kritis"]).size().unstack(fill_value=0)
#     fig, ax = plt.subplots(figsize=(10, 6))
#     sns.heatmap(critical_matrix, annot=True, cmap="Oranges", fmt="d", ax=ax)
#     st.pyplot(fig)

# # --- Visualisasi 5 ---
# elif option == "5. Tren Harian PM2.5 per Stasiun":
#     st.subheader("📈 Tren Harian PM2.5 per Stasiun")
#     pm25 = df[df["parameter_pencemar_kritis"] == "PM25"]
#     pivot_pm25 = pm25.pivot_table(index="bulan", columns="stasiun", values="pm_duakomalima")
#     fig, ax = plt.subplots(figsize=(12, 6))
#     sns.heatmap(pivot_pm25.T, cmap="Reds", cbar_kws={'label': 'PM2.5 (µg/m³)'}, ax=ax)


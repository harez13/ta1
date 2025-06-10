import streamlit as st
import pandas as pd
import joblib

# Judul aplikasi
st.title("Aplikasi Prediksi dengan Model Machine Learning (.joblib)")

# Load model
@st.cache_resource
def load_model():
    return joblib.load("Models/Best_Model.joblib")

model = load_model()

# Input dari pengguna
st.header("Masukkan Nilai Parameter:")

pm10_val = st.number_input("PM10", min_value=0.0, max_value=1000.0, value=50.0)
pm25_val = st.number_input("PM2.5", min_value=0.0, max_value=1000.0, value=30.0)
so2_val = st.number_input("Sulfur Dioksida (SO2)", min_value=0.0, max_value=1000.0, value=10.0)
co_val = st.number_input("Karbon Monoksida (CO)", min_value=0.0, max_value=1000.0, value=5.0)
o3_val = st.number_input("Ozon (O3)", min_value=0.0, max_value=1000.0, value=20.0)
no2_val = st.number_input("Nitrogen Dioksida (NO2)", min_value=0.0, max_value=1000.0, value=8.0)
max_val = st.number_input("Nilai Maksimum ISPU", min_value=0.0, max_value=1000.0, value=55.0)

# Membuat dataframe dari input
input_df = pd.DataFrame([{
    "pm10": pm10_val,
    "pm25": pm25_val,
    "so2": so2_val,
    "co": co_val,
    "o3": o3_val,
    "no2": no2_val,
    "max": max_val
}])

# Tampilkan input
st.subheader("Data yang Dikirim ke Model:")
st.write(input_df)

# Prediksi
if st.button("Prediksi"):
    try:
        prediction = model.predict(input_df)
        st.success(f"Hasil Prediksi: {prediction[0]}")
    except Exception as e:
        st.error("Terjadi kesalahan saat prediksi. Pastikan fitur input sesuai dengan model.")
        st.exception(e)

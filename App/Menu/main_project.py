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

# Input data dari user
st.header("Masukkan Data untuk Prediksi")

# Contoh input fitur (ubah sesuai fitur model Anda)
pm10 = st.number_input("PM10", min_value=0.0, max_value=500.0, value=50.0)
pm25 = st.number_input("PM2.5", min_value=0.0, max_value=500.0, value=30.0)
so2 = st.number_input("Sulfur Dioksida (SO2)", min_value=0.0, max_value=500.0, value=10.0)
co = st.number_input("Karbon Monoksida (CO)", min_value=0.0, max_value=500.0, value=5.0)

# Dataframe input
input_df = pd.DataFrame({
    "pm10": [pm10],
    "pm25": [pm25],
    "so2": [so2],
    "co": [co]
})

# Tampilkan data input
st.subheader("Data yang Anda Masukkan")
st.write(input_df)

# Prediksi
if st.button("Prediksi"):
    prediction = model.predict(input_df)
    st.success(f"Hasil Prediksi: {prediction[0]}")

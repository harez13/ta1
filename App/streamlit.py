# Library
import streamlit as st
import joblib
from PIL import Image
from datetime import datetime
import pytz
from pytz import timezone
import base64

# Memanggil best model
Model = joblib.load("Models/Best_Model.joblib")

# Fungsi untuk mendapatkan string base64 dari file gambar
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Fungsi untuk mengatur gambar lokal sebagai latar belakang halaman
def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    body {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    opacity: 0.86;
    }
    </style>
    ''' % bin_str

    st.markdown(page_bg_img, unsafe_allow_html=True)

# Menggunakan fungsi di atas
set_png_as_page_bg('Images/DKI.jpeg')

# Judul aplikasi
st.markdown("<h1 style='text-align: center;'>Prediksi Kualitas Udara Jakarta</h1>", unsafe_allow_html=True)
st.write("\n\n\n\n\n\n\n\n") 

# Sidebar contact
with st.sidebar:
    st.title("Contact")
    st.write("")
    st.sidebar.markdown("**Phone** +6285727600672")
    st.write("")
    st.sidebar.markdown("**Email** riyanzaenal411@gmail.com")
    st.write("")
    st.sidebar.markdown("**Github** https://github.com/RiyZ411")
    st.write("")
    st.sidebar.markdown("**Linkedin** https://www.linkedin.com/in/riyan-zaenal-arifin-38a587241/")
   
# Container
with st.container():   
    # Layout dengan tiga kolom
    col1, col2, col3 = st.columns(3, gap="large")
    with col1:
        tempat = ["DKI1 Bundaran HI", "DKI2 Kelapa Gading", "DKI3 Jagakarsa", "DKI4 Lubang Buaya", "DKI5 Kebun Jeruk"]
        pilihan = st.selectbox('Pilih Tempat', tempat)
    
    # Form untuk jam
    with col2:
        tz = pytz.timezone('Asia/Jakarta')
        waktu_saat_ini = datetime.now(tz)
        jam_sek = waktu_saat_ini.strftime("%H:%M")
        jam = st.text_input('Pilih Jam\n\n', jam_sek)
        
    # Form tanggal
    with col3:
        tz = pytz.timezone('Asia/Jakarta')
        waktu_saat_ini = datetime.now(tz)
        tgl_sek = waktu_saat_ini.date()
        tgl = st.date_input('Pilih Tanggal\n\n', tgl_sek)


st.write("\n\n\n\n")   
# Form predict
with st.form("predict"):
    # Layout dengan dua kolom
    col1, col2 = st.columns(2, gap="large")
        
    # Form untuk PM10
    with col1:
        pm10_val = st.number_input("Masukkan nilai PM10", min_value=0.0, max_value=1000.0, step=1.0)

    # Form untuk PM25
    with col2:
        pm25_val = st.number_input("Masukkan nilai PM2.5", min_value=0.0, max_value=1000.0, step=1.0)

    # Form untuk O3
    with col1:
        o3_val = st.number_input("Masukkan nilai Ozon (O3)", min_value=0.0, max_value=1000.0, step=1.0)

    # Form untuk SO2
    with col2:
        so2_val = st.number_input("Masukkan nilai Sulfur Dioksida (SO2)", min_value=0.0, max_value=1000.0, step=1.0)

    # Form untuk NO2
    with col1:
        no2_val = st.number_input("Masukkan nilai Nitrogen Dioksida (NO2)", min_value=0.0, max_value=1000.0, step=1.0)

    # Form untuk CO
    with col2:
        co_val = st.number_input("Masukkan nilai Karbon Monoksida (CO)", min_value=0.0, max_value=1000.0, step=1.0)

    # Form untuk max
    with col1:
        max_val = st.number_input("Masukkan nilai max", min_value=0.0, max_value=1000.0, step=1.0)

    with col2:
        param = ["PM10", "PM25", "SO2", "CO", "O3", "NO2"]
        pilihan = st.selectbox('Masukkan Parameter Pencemar Kritis', param)

    # Tambahkan tombol
    submitted = st.form_submit_button("Predict")

        # Lakukan prediksi
    if submitted:
        if pm10_val == 0 or pm25_val == 0 or o3_val == 0 or so2_val == 0 or no2_val == 0 or co_val == 0 or max_val == 0:
            st.error('Mohon diulangi, pastikan semua form telah Anda isi')
        else:
            pred = Model.predict([[pm10_val,pm25_val,so2_val,co_val,o3_val,no2_val,max_val]])
            if pred[0]==1:
                st.success("Kondisi Udara Baik")
            elif pred[0]==2:
                st.warning("Peringatan, Kondisi Udara Sedang")
            elif pred[0]==3:
                st.error("Bahaya, Kondisi Udara Tidak Sehat", icon="⚠️")
        

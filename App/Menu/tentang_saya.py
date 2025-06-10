import streamlit as st
from PIL import Image
import requests
import base64


st.set_page_config(page_title="About Me", layout="centered")

# # Fungsi untuk mendapatkan string base64 dari file gambar
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# # Fungsi untuk mengatur gambar lokal sebagai latar belakang halaman
def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    body {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
    opacity : 0.4;
    }
    </style>
    ''' % bin_str

    st.markdown(page_bg_img, unsafe_allow_html=True)

# # Menggunakan fungsi di atas
set_png_as_page_bg('Images/tom-barrett--bSucp2nUdQ-unsplash (1).jpg')

# Judul
st.title("👤 About Me")

# Gambar dari Google Drive
image_url = "https://drive.google.com/uc?export=view&id=1CdX1Ke8ybf_L9WRgTPd9dQPZi2AgeOfN"
response = requests.get(image_url, stream=True)
img = Image.open(response.raw)

# Layout kolom
col1, col2 = st.columns([1, 2])
with col1:
    st.image(img, caption="Foto Profil", width=200)
with col2:
    st.subheader("Nama Lengkap")
    st.write("👨‍💼 **Posisi**: Analis Kualitas Udara")
    st.write("🏢 **Instansi**: Dinas Lingkungan Hidup")
    st.write("📧 **Email**: nama@email.com")
    st.write("📍 **Lokasi**: Jakarta, Indonesia")

st.markdown("---")

# Penjelasan
st.markdown("""
### ✨ Tentang Saya
Saya seorang analis lingkungan yang fokus pada pemantauan dan analisis kualitas udara, serta pengembangan dashboard interaktif berbasis data.

### 🛠️ Keahlian
- Python, Streamlit, Plotly
- Visualisasi Data Lingkungan
- Pemodelan & Analisis Kualitas Udara
""")
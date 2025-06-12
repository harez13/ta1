import streamlit as st
from PIL import Image
import requests
import base64

# st.set_page_config(layout="wide")
# st.set_page_config(page_title="About Me", layout="centered")


# Judul
st.title("👤 Tentang Saya")

# Gambar dari Google Drive
image_url = "https://drive.google.com/uc?export=view&id=1CdX1Ke8ybf_L9WRgTPd9dQPZi2AgeOfN"
response = requests.get(image_url, stream=True)
img = Image.open(response.raw)

# Layout kolom
col1, col2 = st.columns([1, 2])
with col1:
    st.image(img, caption="Foto Profil", width=200)
with col2:
    st.subheader("Nama Lengkap : Hae Reza Putra Bhakti")
    st.write("👨‍💼 **NPM**: 202143501715")
    st.write("🏢 **Prodi**: Teknik Informatika")
    st.write("📧 **Email**: haerezaputra6@gmail.com.com")
    st.write("📍 **No. HP**: 0895705701052")

st.markdown("---")

# Penjelasan
st.markdown("""
### ✨ Tentang Saya
Saya adalah mahasiswa tingkat akhir pada Universitas Indraprasta PGRI. Web 'Prediksi Kualitas Udara Jakarta' ini merupakan tugas akhir saya
""")


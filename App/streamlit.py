# Library
import streamlit as st

import base64

# Fungsi untuk mengonversi gambar ke base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Konversi gambar lokal ke base64
bg_image = get_base64_of_bin_file("App\tom-barrett--bSucp2nUdQ-unsplash (1).jpg")  # Ganti dengan nama file kamu

# Sisipkan CSS untuk ubah background halaman utama (tanpa sidebar)
st.markdown(
    f"""
    <style>
        [data-testid="stAppViewContainer"] > .main {{
            background-image: url("data:image/jpg;base64,{bg_image}");
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# -- Page Setup --

tentang_saya = st.Page(
    'Menu/tentang_saya.py',
    title = 'Tentang Saya',
)

homepage = st.Page(
    'Menu/homepage.py',
    title = 'Homepage',
    default=True
)

dataset = st.Page(
    'Menu/dataset.py',
    title = 'Dataset',
)

project1_page = st.Page(
    'Menu/main_project.py',
    title = 'Project',
)

project2_page = st.Page(
    'Menu/dashboard.py',
    title = 'Dashboard',
)

#-- Navigation Setup [Without Sections] --
# pg = st.navigation(pages = [tentang_saya, project1_page, project2_page])

#-- Navigation Setup With Sections
pg = st.navigation(
    {
        'Info' : [tentang_saya, homepage],
        'Projects' : [project1_page, project2_page, dataset]
    }
)



# pages = {
#     'Info' : [
#         st.Page('Menu/tentang_saya.py', title='Tentang Saya')
#     ],
#     'Projects' : [
#         st.Page('Menu/dashboard.py', title='Dashboard')
#     ]
# }

# pg = st.navigation(pages)

#-- Run Navigation
pg.run()
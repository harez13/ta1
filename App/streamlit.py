# Library
import streamlit as st
import base64

st.set_page_config(layout="wide")

import os



# Fungsi untuk mengubah file gambar lokal jadi base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Masukkan path ke file gambar lokal kamu (contoh: "background.jpg")
image_path = "Images/abhishek-koli-DsxD_bTq8x0-unsplash.jpg"
background_image_base64 = get_base64_of_bin_file(image_path)

# Sisipkan CSS ke Streamlit
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{background_image_base64}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
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


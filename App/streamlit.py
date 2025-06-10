# Library
import streamlit as st
import base64

st.set_page_config(layout="wide")

import os


# === Ganti nama file dengan file kamu ===
file_path = "Images/tom-barrett--bSucp2nUdQ-unsplash (1).jpg"

def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

if os.path.exists(file_path):
    bg_image = get_base64(file_path)

    st.markdown(
        f"""
        <style>
        /* Background untuk seluruh halaman termasuk header */
        html, body {{
            height: 100%;
            background: none;
        }}

        body::before {{
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background-image: url("data:image/png;base64,{bg_image}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            opacity: 1;
            z-index: -1;
        }}

        /* Overlay semi-transparan untuk area konten utama */
        [data-testid="stAppViewContainer"] > .main::before {{
            content: "";
            position: absolute;
            top: 0;
            bottom: 0;
            right: 0;
            left: 0;
            background-color: rgba(0, 0, 0, 0.4);
            z-index: 0;
        }}

        /* Konten tetap tampil di atas overlay */
        [data-testid="stAppViewContainer"] > .main > div {{
            position: relative;
            z-index: 1;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
else:
    st.error("Gambar tidak ditemukan.")

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


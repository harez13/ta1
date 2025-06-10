# Library
import streamlit as st
import base64

st.set_page_config(layout="wide")


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

# Fungsi untuk konversi gambar lokal ke base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Ganti dengan nama file gambar lokal kamu
sidebar_bg = get_base64_of_bin_file("Images/tom-barrett--bSucp2nUdQ-unsplash (1).jpg")

# Sisipkan CSS untuk sidebar
st.markdown(
    f"""
    <style>
        [data-testid="stSidebar"] {{
            background-image: url("data:image/jpg;base64,{sidebar_bg}");
            background-size: cover;
            background-position: center;
            opacity: 0.8;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

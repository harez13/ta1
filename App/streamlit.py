# Library
import streamlit as st
import joblib
from PIL import Image
from datetime import datetime
import pytz
from pytz import timezone
import base64


st.title('Test')

# -- Page Setup --

tentang_saya = st.Page(
    'Menu/tentang_saya.py',
    title = 'Tentang Saya',
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
        'Info' : [tentang_saya],
        'Projects' : [project1_page, project2_page]
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
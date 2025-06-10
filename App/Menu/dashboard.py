import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from streamlit_gsheets import GSheetsConnection

conn = st.connection('gsheets', type=GSheetsConnection)

df=conn.read()

st.write(df)


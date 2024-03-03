import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="Lockness",
    page_icon="🔒",
    layout="wide",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': "Lockness is a platform that allows you to upload your data and machine learning models to keep them safe."
    },
    initial_sidebar_state="auto"
)

st.image('./images/lockness.png', width=200)
st.header("Welcome to Lockness", divider='grey')


st.subheader("What do you want to do?")
col1, col2 = st.columns(2)
with col1:
    go_to_browse_data = st.button("Browse Datasets")
    if go_to_browse_data:
        switch_page("Browse_Datasets")
with col2:
    go_to_browse_model = st.button("Browse Models")
    if go_to_browse_model:
        switch_page("Browse_Model")

st.divider()
st.subheader("What do you own?")
col1, col2 = st.columns(2)
with col1: 
    go_to_upload_data = st.button("Data")
    if go_to_upload_data:
        switch_page("Upload_data")
with col2:
    go_to_upload_model = st.button("A Machine Learning Model")
    if go_to_upload_model:
        switch_page("Upload_model")
    
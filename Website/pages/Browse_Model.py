import streamlit as st

st.set_page_config(
    page_title="Lockness",
    page_icon="🔒",
    layout="wide",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': "Lockness is a platform that allows you to upload your data and machine learning models to keep them safe."
    }
)


st.title("Find all the uploaded models here")

with open('models.txt', 'r') as f:
    models = f.readlines()
    st.write(models)
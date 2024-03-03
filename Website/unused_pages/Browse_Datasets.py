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

st.title("Find all the uploaded datsets here")

search_dataset = st.text_input("Search for a dataset")

with open ('datasets.txt', 'r') as f:
    datasets = f.readlines()
    
if search_dataset:
    datasets = [dataset for dataset in datasets if search_dataset.lower() in dataset.lower()]

for dataset in datasets:
    st.write(dataset)
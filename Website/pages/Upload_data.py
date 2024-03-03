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

st.header("Upload Your Encrypted Data Here")

new_dataset_name = st.text_input("Enter the name of your Dataset here")
new_dataset = st.file_uploader("Upload your data here") 
 
if new_dataset:
    st.write(f'Your data has been uploaded successfully as "{new_dataset_name}"!')
    with open('datasets.txt', 'a') as f:
        f.write(f'{new_dataset_name}\n')
        
    f.close()


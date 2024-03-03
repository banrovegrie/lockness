import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page


custom_css = """
<style>
    /* Target the button within the app */
    .stButton>button {
        background-color: #FFF;
        color: black;  
        padding: 10px 24px; 
        font-size: 20px; 
        border: 2px solid black; 
        border-radius: 5px; 
        cursor: pointer; 
        margin: 10px 0; 
    }
    /* Change hover effect */
    .stButton>button:hover {
        background-color: #000;
        color: white;
    }
</style>
"""

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

st.markdown(custom_css, unsafe_allow_html=True)


st.subheader("What do you want to do?")

col1, col2 = st.columns(2)
with col1:
    go_to_browse_model = st.button("Browse Models")
    if go_to_browse_model:
        switch_page("Browse_Model")

with col2 :    
    go_to_upload_model = st.button("Upload a Machine Learning Model")
    if go_to_upload_model:
        switch_page("Upload_model") 



# col1, col2, col3 = st.columns(3)
# with col1:
#     go_to_browse_data = st.button("Browse Datasets")
#     if go_to_browse_data:
#         switch_page("Browse_Datasets")
        
#     # st.divider()
  
#     go_to_browse_model = st.button("Browse Models")
#     if go_to_browse_model:
#         switch_page("Browse_Model")
   
#     # st.divider()
    
    
    
# with col2:
   
#     go_to_upload_model = st.button("Upload a Machine Learning Model")
#     if go_to_upload_model:
#         switch_page("Upload_model")      
#     # st.divider()
  
#     go_to_upload_data = st.button("Upload a Dataset")
#     if go_to_upload_data:
#         switch_page("Upload_data")
#     # st.divider()
        
    
    
# with col3:
    
#     train_model = st.button("Train a model")
#     if train_model:
#         switch_page("Training")
#     # st.divider()
    
#     do_inference = st.button("Do inference on a model")
#     if do_inference:
#         switch_page("Inference")    
#     # st.divider()
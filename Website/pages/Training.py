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

st.title("Train your model here")
st.divider( )

st.subheader("Choose or upload the model that you want to train")

col1, col2, col3 = st.columns(3)

with col1:
    model_name =  st.selectbox("Choose a model", ["Random Forest", "Decision Tree", "SVM", "KNN", "Logistic Regression"], index=None, placeholder="Choose a model")
    
with col2:
    st.markdown("<h1 style='text-align: center;'>OR</h1>", unsafe_allow_html=True)

    
with col3:
    uploaded_model_name = st.file_uploader("Upload your model here")


st.divider( )
st.subheader("Choose or upload the data that you want to use to train the model")
col1, col2, col3 = st.columns(3)
with col1:
    dataset_name = st.selectbox("Choose a dataset", ["Iris", "Titanic", "Breast Cancer", "Wine"], index=None, placeholder="Choose a dataset")
    
with col2:
    st.markdown("<h1 style='text-align: center;'>OR</h1>", unsafe_allow_html=True)

    
with col3:
    uploaded_dataset_name = st.file_uploader("Upload your data here")



if (model_name or uploaded_model_name)  and (dataset_name or uploaded_dataset_name):
    st.button("Train!")

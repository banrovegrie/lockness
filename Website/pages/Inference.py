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


st.header("Inference")

st.subheader("Choose the model that you want to use")

option = st.selectbox("Choose a model", ["Random Forest", "Decision Tree", "SVM", "KNN", "Logistic Regression"], index=None, placeholder="Choose a model")

st.write("You selected:", option)


st.divider()

st.text_input("Enter the data that you want to use to make the prediction here")


st.button("Predict")

st.divider()

st.write("The prediction is: ")

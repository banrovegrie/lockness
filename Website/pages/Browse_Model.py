import streamlit as st
import json
import pickle

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
search_model = st.text_input("Search for a model")


with open('models.txt', 'r') as f:
    models = f.readlines()
    
if search_model:
    models = [model for model in models if search_model.lower() in model.lower()]
    models.append("None")


selected_model = st.selectbox("Select a model", models)

st.divider()

if selected_model and selected_model != "None":
    st.write(f"You have selected {selected_model}!") 
    
    dataset_type = st.radio("What do you want to inference on?", ["None", "Single Point", "Whole Dataset"], captions = ["","Enter a point on which you want to do inference on", "Upload the whole dataset you want to do inference on"])
    
    st.divider()

    if dataset_type == "Single Point":
        input_model = st.text_input("Enter the point here")
        
        # prediction = selected_model.predict(input_model)
        # st.write(f"The prediction for the given input is {prediction}")
        
        
    elif dataset_type == "Whole Dataset":
        dataset = st.file_uploader("Upload the dataset here")
        predictions = ["ffFff", "ff","Ffff"]
        show_download_button = False
        # for point in dataset:
        #     prediction = selected_model.predict(point)
        #     predictions.append(prediction)
    
        show_download_button = True

        # give the option to download the predictions
        if show_download_button:
            st.write(f"The predictions are ready to be downloaded")
            predictions = json.dumps(predictions)
            st.download_button(
            label="Download predictions as CSV",
            data=predictions,
            file_name='large_df.csv',
            mime='text/csv',
        )        
        
                
    
        


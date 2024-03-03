import streamlit as st
import json

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


st.header("Upload Your Encrypted Model Here")

new_model_name = st.text_input("Enter the name of your model here")
new_model_description = st.text_area("Enter a description of your model here")
new_model = st.file_uploader("Upload your model here")
save_model = st.button("Save model")

if new_model and save_model and new_model_name:
    st.write(f'Your model has been uploaded successfully as "{new_model_name}"!')
    with open('models.txt', 'a') as f:
        f.write(f'{new_model_name}\n')
        
    # open the model_description.json and add another key pair where the key is the model name with the value being the description
    with open('model_description.json', 'r') as f:
        data = json.load(f)
        data[new_model_name] = new_model_description
        f.close()
    with open('model_description.json', 'w') as f:
        json.dump(data, f)
        f.close()
        
    # save the model
    with open(f'models/{new_model_name}.pkl', 'wb') as f:
        f.write(new_model.read())
        
    f.close()

else : 
    st.error("Please enter the name of the model and upload the file before saving it.")
    
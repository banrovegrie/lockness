import streamlit as st
# from navbar import render_navbar  # Ensure this function is properly set up to return navigation HTML

def main():
    # Reuse the same CSS for styling
    custom_css = """
    <style>
    body {
        margin: 0;
        font-family: Arial, sans-serif;
        background-color: #001f3f; /* Dark Navy Blue */
        color: white; /* White text */
    }
    .header-panel {
        padding: 20px 50px;
        background: linear-gradient(to right, #004d40, #008080); /* Dark teal to lighter teal gradient */
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .header-title {
        font-size: 24px;
    }
    .icon-button {
        background: none;
        border: none;
        color: #FFC0CB;
        font-size: 16px;
        padding: 10px 20px;
        cursor: pointer;
        text-decoration: none;
        transition: background-color 0.3s ease;
    }
    .icon-button:hover {
        background-color: #003d40;
    }
    .main-content {
        padding: 20px 50px;
    }
    .upload-btn {
        background-color: #008080;
        color: white;
        border: none;
        padding: 8px 16px;
        border-radius: 5px;
        transition: opacity 0.3s ease;
    }
    .upload-btn:hover {
        opacity: 0.8;
    }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

    # Main Content for Model Upload
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    st.subheader("Compile Your Model Using LockNess Compiler")
    st.markdown("Compile your model for optimization for deployment. [Visit this page for complete instructions](#). Note that you can do all of this on the CLI, and is highly preferred!")

    st.subheader("Upload Your Machine Learning Model")
    st.write("You can also upload your model file here. Acceptable file formats include `.h5`, `.pt`, `.onnx`, etc.")
    uploaded_file = st.file_uploader("Choose a file", type=["h5", "pt", "onnx"])
    if uploaded_file is not None:
        # Process the file here (the actual processing logic will depend on your backend setup)
        st.success("File successfully uploaded!")
        st.write(f"Uploaded file name: {uploaded_file.name}")

    st.subheader("CLI Upload Instructions")
    st.code("""
    # Install the Lockness package
    pip install lockness

    # Add your username to the Lockness config
    lockness -add username

    # Compile your model
    lockness -compile xyz_model.pkl -y

    # Push the model to the server
    lockness push -n "Your Model Name"
    """)

    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()

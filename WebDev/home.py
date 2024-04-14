import streamlit as st
import base64

def main():
    # Custom CSS for full-page and enhanced color styling
    custom_css = """
    <style>
    body {
        margin: 0;
        font-family: Arial, sans-serif;
        background-color: #2E2F2F; /* Dark Navy Blue */
        color: white; /* White text */
        text-align: center; /* Center-align text */
    }
    .header-panel {
        padding: 20px 50px;
        background: linear-gradient(to right, #004d40, #008080); /* Dark teal to lighter teal gradient */
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .logo-container {
        text-align: center; /* Center logo container */
        margin-top: 2rem;
    }
    .logo {
        width: 200px; /* Set logo width */
        margin: auto; /* Center logo horizontally */
    }
    .lockness-title {
        font-size: 2rem; /* Larger font size for title */
        font-weight: bold; /* Bold font weight for title */
        margin: 0.5rem 0; /* Margin above and below title */
    }
    .blurb {
        font-size: 1.25rem; /* Font size for the blurb */
        margin-bottom: 2rem; /* Space below the blurb */
    }
    </style>
    """ 
    st.markdown(custom_css, unsafe_allow_html=True)

    # Logo and blurb
    st.markdown("""
    <div class="logo-container">
        <img src="data:image/png;base64,{}" class="logo">
        <div class="lockness-title">LockNess</div>
        <p class="blurb">Securely build the best machine learning models with new data</p>
    </div>
    """.format(logo_to_base64('WebDev/logo.png')), unsafe_allow_html=True)

    if st.button('Explore Datasets'):
        st.session_state.page = "Explore Datasets"

def logo_to_base64(path):
    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

if __name__ == "__main__":
    main()

import streamlit as st

def render_navbar():
    navbar_html = """
    <div class="nav-bar">
        <button onclick="window.location.href = 'upload_model_page.py';" class="icon-button">+ Upload Model</button>
        <button onclick="window.location.href = 'lease_dataset_page.py';" class="icon-button">Lease a Dataset</button>
        <button onclick="window.location.href = 'user_profile_page.py';" class="icon-button">Profile</button>
    </div>
    """
    return navbar_html

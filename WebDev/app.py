
import streamlit as st
from home import main as home_main
from uploadmodel import main as upload_main
from details import main as lease_main
from profile_page import main as profile_main
from explore_datasets_page import main as explore_main
from help import main as help_main
# def main():
#     # Setup navigation
#     pages = {
#         "Home": home_main,
#         "Upload Model": upload_main,
#         "Lease Dataset": lease_main,
#         "User Profile": profile_main
#     }

#     # Define CSS for the sidebar
#     st.sidebar.markdown("""
#     <style>
#     .sidebar .sidebar-content {
#         background-color: #004d40 !important; /* Teal background for the whole sidebar */
#     }
#     a:only-child {
#         display: block;
#         color: black; /* White text for all items */
#         padding: 10px;
#         font-size: 18px; /* Larger font size */
#         text-align: left;
#         text-decoration: none; /* No underlines */
#     }
#     a:only-child:hover {
#         background-color: #000000; /* Black background on hover */
#         color: #FFC0CB; /* Pink text on hover */
#     }
#     </style>
#     """, unsafe_allow_html=True)

#     # Sidebar with navigation as clickable text
#     st.sidebar.title("Navigation")
#     for page_name in pages.keys():
#         page_func = pages[page_name]
#         # Use markdown links styled as block elements
#         st.sidebar.markdown(f'<a href="#" onclick="handleNavClick(\'{page_name}\');">{page_name}</a>', unsafe_allow_html=True)

#     # JavaScript to handle clicks and prevent default link behavior
#     st.markdown("""
#     <script>
#     function handleNavClick(pageName) {
#         window.parent.postMessage({
#             type: 'streamlit:setComponentValue',
#             key: 'page',
#             value: pageName
#         }, '*');
#     }
#     </script>
#     """, unsafe_allow_html=True)

#     # Check session state for page to display
#     if 'page' in st.session_state:
#         pages[st.session_state.page]()
#     else:
#         # Default page
#         home_main()

# if __name__ == "__main__":
#     main()

import streamlit as st
from home import main as home_main
from uploadmodel import main as upload_main
from details import main as lease_main
from profile_page import main as profile_main

def main():
    # Define CSS for the sidebar
    st.sidebar.markdown("""
    <style>
    .sidebar .sidebar-content {
        background-color: #004d40; /* Teal background for the whole sidebar */
        border-radius: 0.5rem; /* Rounded corners for the sidebar */
        color: white; /* White text for the sidebar */
    }
    /* Custom style for sidebar navigation items */
    .clickable {
        margin: 0.5rem 0;
        display: block;
        font-size: 1.25rem;
        color: white;
    }
    .clickable:hover {
        background-color: #003d40; /* Darker teal background on hover */
        color: #FFC0CB; /* Pink text on hover */
        border-radius: 0.5rem;
    }
    </style>
    """, unsafe_allow_html=True)

    # Setup sidebar navigation
    st.sidebar.title("Navigation")
    pages = {
        "Home": home_main,
        "Upload Model": upload_main,
        "Lease Dataset": lease_main,
        "User Profile": profile_main,
        "Explore Datasets": explore_main,
        "Profile": profile_main,
        "Help": help_main
    }
    
    # Display navigation links
    for page_name, page_func in pages.items():
        if st.sidebar.button(page_name, key=page_name, on_click=lambda pn=page_name: set_page(pn)):
            # This will display the selected page by updating the session state
            pass

    # Initialize the page state if it doesn't exist
    if 'page' not in st.session_state:
        st.session_state.page = 'Home'

    # Call the page function from the session state
    pages[st.session_state.page]()

def set_page(page_name):
    """Set the page to display."""
    st.session_state.page = page_name

if __name__ == "__main__":
    main()

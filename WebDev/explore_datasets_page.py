import streamlit as st
# from navbar import render_navbar  # Import the navbar function
def main():
    # Custom CSS for full-page and enhanced color styling
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
        font-size: 24px; /* Larger font size for title */
    }
    
    .icon-button {
        background: none;
        border: none;
        color: #FFC0CB; /* Pastel Pink */
        font-size: 16px;
        padding: 10px 20px;
        cursor: pointer;
        text-decoration: none;
        transition: background-color 0.3s ease;
    }
    .icon-button:hover {
        background-color: #003d40; /* Very dark teal on hover */
    }
    .main-content {
        display: flex;
        justify-content: space-between;
        padding: 20px 50px; /* Padding for main content */
        margin-top: 20px;
    }
    .blurb {
        flex: 1; /* Flexible space usage */
        padding-right: 20px;
    }
    .big-text {
        flex: 1;
        font-size: 24px;
        text-align: left;
        padding-left: 20px;
    }
    button {
        background-color: #008080; /* Teal background */
        color: white;
        border: none;
        padding: 8px 16px;
        border-radius: 5px;
        transition: opacity 0.3s ease;
    }
    button:hover {
        opacity: 0.8;
    }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

    # Define popular datasets
    popular_datasets = [
        {'name': 'MNIST', 'image': 'https://via.placeholder.com/150', 'size': 20, 'num_samples': 70000, 'price_per_unit': 5},
        {'name': 'CIFAR-10', 'image': 'https://via.placeholder.com/150', 'size': 25, 'num_samples': 60000, 'price_per_unit': 4},
        {'name': 'ImageNet', 'image': 'https://via.placeholder.com/150', 'size': 1024, 'num_samples': 1400000, 'price_per_unit': 20},
        {'name': 'Titanic', 'image': 'https://via.placeholder.com/150', 'size': 1, 'num_samples': 891, 'price_per_unit': 2},
        {'name': '20 Newsgroups', 'image': 'https://via.placeholder.com/150', 'size': 15, 'num_samples': 18846, 'price_per_unit': 3}
    ]

    # Filter sidebar
    st.sidebar.header('Filter Options')
    num_samples = st.sidebar.slider('Number of Samples', 100, 1000000, (1000, 50000))
    data_type = st.sidebar.multiselect('Data Type', ['Images', 'Text', 'Tabular', 'Time Series'])
    domain = st.sidebar.multiselect('Domain', ['Healthcare', 'Finance', 'Automotive', 'Retail', 'Technology'])
    price_per_unit = st.sidebar.slider('Price per Unit', 0, 100, (5, 20))

    # Main content area for datasets
    datasets = get_datasets(popular_datasets)
    num_cols = 3
    num_rows = (len(datasets) + num_cols - 1) // num_cols

    for _ in range(num_rows):
        cols = st.columns(num_cols)
        for col in cols:
            if datasets:
                dataset = datasets.pop(0) if datasets else None
                if dataset:
                    with col:
                        st.markdown(f"<div class='dataset-card'>", unsafe_allow_html=True)
                        st.image(dataset['image'], use_column_width=True)
                        st.markdown(f"### {dataset['name']}")
                        st.markdown(f"**Size**: {dataset['size']} MB")
                        st.markdown(f"**Samples**: {dataset['num_samples']}")
                        st.markdown(f"**Price/Unit**: ${dataset['price_per_unit']}")
                        # st.button("Explore", key=f"explore_{dataset['name']}")
                        if st.button("Explore", key=f"explore_{dataset['name']}"):
                            st.session_state.page = "Lease Dataset"
                        st.markdown("</div>", unsafe_allow_html=True)

def get_datasets(custom_datasets):
    # This function returns a list of datasets
    return custom_datasets

if __name__ == "__main__":
    main()

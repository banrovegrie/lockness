# import streamlit as st

# def main():
#     st.markdown(get_custom_css(), unsafe_allow_html=True)

#     # Layout to simulate sticky behavior
#     top_section = st.empty()  # Placeholder for sticky-like button

#     # Assuming dynamic selection, use a session state to simulate
#     if 'selected_dataset' not in st.session_state:
#         st.session_state.selected_dataset = {
#             'name': 'MNIST',
#             'uploader': 'OpenAI',
#             'rating': '4.5/5',
#             'description': 'MNIST is a large database of handwritten digits used for image processing systems.',
#             'metrics': {'Accuracy': '99.5%', 'Loss': '0.015'},
#             'model_compatibility': ['Model A', 'Model B', 'Model C'],
#             'additional_info': 'Ideal for developing proof-of-concept models that demonstrate handwriting recognition capabilities.'
#         }

#     dataset = st.session_state.selected_dataset

#     # Action button in the top section
#     with top_section.container():
#         if st.button("Rent/Lease/Use Dataset for $5", key="rent_dataset"):
#             st.success(f"You are now renting/leasing/using the {dataset['name']} dataset!")
#             st.session_state.rented = True
#         if 'rented' in st.session_state and st.session_state.rented:
#             st.info(f"Dataset ID {dataset['name']} is: `wsdfjheabsjhd567fBEDGHJFBWJHFASFNBSFH`. Copy paste when prompted on your terminal.")

#     # Main content
#     st.title(dataset['name'])
#     st.subheader("Dataset Details")
#     st.write(f"Uploader: {dataset['uploader']}")
#     st.write(f"Rating: {dataset['rating']}")
#     st.write(f"Description: {dataset['description']}")

#     # Compatibility check with model
#     st.markdown("### Compatibility Check with Model")
#     model_options = dataset['model_compatibility']
#     chosen_model = st.selectbox("Choose a model to check compatibility:", model_options)
#     st.write(f"The chosen model, {chosen_model}, is compatible with {dataset['name']}.")

#     st.markdown("### Additional Information")
#     st.write(dataset['additional_info'])

# def get_custom_css():
#     return """
#     <style>
#     body {
#         font-family: Arial, sans-serif;
#         background-color: #001f3f; /* Dark Navy Blue */
#         color: white; /* White text */
#     }
#     .css-2trqyj {
#         background-color: #008080; /* Teal background */
#         border-radius: 5px;
#         border: none;
#     }
#     </style>
#     """

# if __name__ == "__main__":
#     main()

import streamlit as st

def main():
    st.markdown(get_custom_css(), unsafe_allow_html=True)

    # Assuming dynamic selection, use a session state to simulate
    if 'selected_dataset' not in st.session_state:
        st.session_state.selected_dataset = {
            'name': 'MNIST',
            'uploader': 'OpenAI',
            'rating': '4.5/5',
            'description': 'MNIST is a large database of handwritten digits used for image processing systems.',
            'metrics': {'Accuracy': '99.5%', 'Loss': '0.015'},
            'model_compatibility': ['Model A', 'Model B', 'Model C'],
            'additional_info': 'Ideal for developing proof-of-concept models that demonstrate handwriting recognition capabilities.',
            'metadata': {
                'Total Samples': '70,000',
                'Classes': '10 (Digits 0-9)',
                'Image Size': '28x28 pixels',
                'File Format': 'CSV',
                'Storage Size': '15 MB'
            }
        }

    dataset = st.session_state.selected_dataset

    # Action button in the top section
    with st.container():
        if st.button("Rent/Lease/Use Dataset for $5", key="rent_dataset"):
            st.success(f"You are now renting/leasing/using the {dataset['name']} dataset!")
            st.session_state.rented = True
        if 'rented' in st.session_state and st.session_state.rented:
            st.info(f"Dataset ID {dataset['name']} is: `wsdfjheabsjhd567fBEDGHJFBWJHFASFNBSFH`. Copy paste when prompted on your terminal.")

    # Main content
    st.title(dataset['name'])
    st.subheader("Dataset Details")
    st.write(f"Uploader: {dataset['uploader']}")
    st.write(f"Rating: {dataset['rating']}")
    st.write(f"Description: {dataset['description']}")

    # Metadata
    st.subheader("Metadata")
    for key, value in dataset['metadata'].items():
        st.write(f"**{key}:** {value}")

    # Compatibility check with model
    st.markdown("### Compatibility Check with Model")
    model_options = dataset['model_compatibility']
    chosen_model = st.selectbox("Choose a model to check compatibility:", model_options)
    st.write(f"The chosen model, {chosen_model}, is compatible with {dataset['name']}.")

    st.markdown("### Additional Information")
    st.write(dataset['additional_info'])

    # Download sample dataset button
    if st.button('Download Sample Dataset'):
        # Logic to download the sample dataset
        st.write("Downloading a sample of the MNIST dataset...")  # Placeholder for actual download logic
        st.success("Download successful! Check your downloads folder.")

def get_custom_css():
    return """
    <style>
    body {
        font-family: Arial, sans-serif;
        background-color: #001f3f; /* Dark Navy Blue */
        color: white; /* White text */
    }
    .css-2trqyj {
        background-color: #008080; /* Teal background */
        border-radius: 5px;
        border: none;
    }
    </style>
    """

if __name__ == "__main__":
    main()

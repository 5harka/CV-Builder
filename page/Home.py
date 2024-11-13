
import streamlit as st
from PIL import Image
from menu import menu_sidebar
from streamlit import switch_page
def home_page():
    # Initialize session state
    if 'page' not in st.session_state:
        st.session_state.page = 'home'


    # Display the selected page
    if st.session_state.page == 'home':

        # Main title and description
        st.title("Welcome to the CV Builder 📊")
        st.markdown("""
        ### Streamline Your Workflow
        Navigate through the available options in the sidebar to view your details or add new data using the Form.
        """)
        # Added an image (use_column_width=True) for bigger image
        st.image("https://th.bing.com/th/id/R.7ba5342e2c347f79213120564bf5875e?rik=2C9B5S%2bOtr3kRw&pid=ImgRaw&r=0",
                 caption="Your data, your way.", )

        # Buttons for each page
        col1, col2 = st.columns(2)
        if col1.button("Create a Form"):
            st.session_state.page = "form"
        if col2.button("Update Your Info"):
            st.session_state.page = "display"

        # Footer
        st.markdown("""
        ---
        *how to make a cool line above this text(---)*
        """)
        st.divider()
    elif st.session_state.page == 'form':
        from page.Form import form_page
        form_page()
    elif st.session_state.page == 'display':
        from page.Display import Display
        Display()



# st.set_page_config(page_title='Resume Maker', page_icon='📃', initial_sidebar_state='collapsed')
home_page()









# # Add navigation buttons
# st.subheader("Select an Option")
# col1, col2 = st.columns(2)
#
# with col1:
#     if st.button("Go to Form"):
#         st.experimental_set_query_params(page="1_Form")
#
# with col2:
#     if st.button("View Display"):
#         st.experimental_set_query_params(page="2_Display")

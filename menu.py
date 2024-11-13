import streamlit as st
from streamlit_option_menu import option_menu


def menu_sidebar():
    # Sidebar menu
    with st.sidebar:
        selected = option_menu(
            menu_title="Main Menu",
            options=["Home", "Form", "Display"],
            icons=["house", "file-earmark-text", "display"],
            menu_icon="cast",
            default_index=0,  # optional Highlights the First result(Home)
        )

    # Navigation logic
    if selected == "Home":
        from page.Home import home_page
        home_page()
    elif selected == "Form":
        from page.Form import form_page
        form_page()
    elif selected == "Display":
        from page.Display import Display
        Display()














    # st.sidebar.title("Navigation")
    # page = st.sidebar.radio("Go to", ["Home", "Form"])
    #
    #
    # if page == "Home":
    #     st.page_link("pages/Home.py", label="Home", icon="🏠")
    # elif page == "Form":
    #     st.page_link("pages/Form.py", label="Form", icon="📝")

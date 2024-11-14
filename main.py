import streamlit as st
import streamlit_authenticator as stauth
from dependancies import sign_up, fetch_users
from models import SessionLocal


from menu import menu_sidebar

st.set_page_config(page_title='Resume Maker', page_icon='📃', initial_sidebar_state='collapsed')

# Logo
st.logo("https://www.dorsch.ae/fileadmin/Logos/global/Logo_DorschGlobal_1000_w.svg")

try:
    with SessionLocal() as db:
        users = fetch_users(db)
        emails = [user.email for user in users]
        usernames = [user.username for user in users]
        passwords = [user.password for user in users]

    credentials = {'usernames': {}}
    for index in range(len(emails)):
        credentials['usernames'][usernames[index]] = {'name': emails[index], 'password': passwords[index]}

    Authenticator = stauth.Authenticate(
        credentials=credentials,
        cookie_name='Streamlit',
        key='abcdef',
        cookie_expiry_days=4
    )

    email, authentication_status, username = Authenticator.login('Log In', 'main')

    info, info1 = st.columns(2)

    if not authentication_status:
        sign_up()

    if username:
        if username in usernames:
            if authentication_status:
                menu_sidebar()
                st.logo("https://www.dorsch.ae/fileadmin/Logos/global/Logo_DorschGlobal_1000_w.svg")
                st.sidebar.subheader(f'Welcome :green[{username}]')
                Authenticator.logout('Log Out', 'sidebar')
            elif not authentication_status:
                with info:
                    st.error('Incorrect Password or username')
            else:
                with info:
                    st.warning('Please feed in your credentials')
        else:
            with info:
                st.warning('Username does not exist, Please Sign up')

except Exception as e:
    st.success('Refresh Page')
    st.error(f'Error: {e}')

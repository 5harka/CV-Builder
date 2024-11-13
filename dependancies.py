import streamlit as st
import streamlit_authenticator as stauth
import datetime
import re
from sqlalchemy.orm import Session
from models import SessionLocal
from crud import insert_user, fetch_users, get_user_emails, get_usernames


def validate_email(email):
    pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    return bool(re.match(pattern, email))

def validate_username(username):
    pattern = "^[a-zA-Z0-9]*$"
    return bool(re.match(pattern, username))

def sign_up():
    with st.form(key='signup', clear_on_submit=True):
        with st.expander("Sign Up"):
            st.subheader(':green[Sign Up]')
            email = st.text_input(':blue[Email]', placeholder='Enter Your Email')
            username = st.text_input(':blue[Username]', placeholder='Enter Your Username')
            password1 = st.text_input(':blue[Password]', placeholder='Enter Your Password', type='password')
            password2 = st.text_input(':blue[Confirm Password]', placeholder='Confirm Your Password', type='password')

            if email:
                if validate_email(email):
                    with SessionLocal() as db:
                        if email not in get_user_emails(db):
                            if validate_username(username):
                                if username not in get_usernames(db):
                                    if len(username) >= 2:
                                        if len(password1) >= 6:
                                            if password1 == password2:
                                                hashed_password = stauth.Hasher([password2]).generate()
                                                insert_user(db, email, username, hashed_password[0])
                                                st.success('Account created successfully!!')
                                                st.snow()
                                            else:
                                                st.warning('Passwords Do Not Match')
                                        else:
                                            st.warning('Password is too Short')
                                    else:
                                        st.warning('Username Too short')
                                else:
                                    st.warning('Username Already Exists')
                            else:
                                st.warning('Invalid Username')
                        else:
                            st.warning('Email Already exists!!')
                else:
                    st.warning('Invalid Email')

            btn1, bt2, btn3, btn4, btn5 = st.columns(5)
            with btn3:
                st.form_submit_button('Sign Up')

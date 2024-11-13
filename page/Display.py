
import sqlite3
import streamlit as st
import pandas as pd
from pandas.core.computation.align import align_terms
from streamlit import text_input

def Display():
    tables = ['employeeInformation','employeeEducation','employeeExperience','TransactionTimestamps']

    def get_database_table(name):
        # Connect to the SQLite database
        conn = sqlite3.connect('.venv/mydatabase10.sqlite')
        query = f"SELECT * FROM {name}"

        # Read the data into a DataFrame
        sql = pd.read_sql_query(query, conn)

        # Display the DataFrame in Streamlit
        st.title(name)
        st.dataframe(sql)

        # Close the database connection
        conn.close()

    def update_employee_information(match):
        col1, col2 = st.columns(2)
        employee_name = col1.write(f"Name is :{match['employee_name'].values[0]}")
        position = col2.write(match['position'].values[0])

        col1, col2 = st.columns(2)
        telephone = col1.write(match['telephone'].values[0])
        email = col2.write(match['email'].values[0])

        col1, col2, col3 = st.columns(3)
        years_of_exp = col1.write(match['years_of_experience'].values[0])
        regional_years_of_exp = col2.write(match['regional_years_of_experience'].values[0])
        years_of_dorsch = col3.write(match['years_with_dorsch'].values[0])

        col1, col2, col3 = st.columns(3)
        nationality = col1.write(match['nationality'].values[0])
        dob = col2.write(match['dob'].values[0])
        marital_status = col3.write(match['marital_status'].values[0])

        col1, col2 = st.columns(2)
        driving_license = col2.write(match['driving_license'].values[0])
        employee_languages = col1.write(match['languages'].values[0])




    st.write("""
    # CV Building Time
    Hello *world!*
    """)

    df = pd.read_csv("C:/Users/Sharmarke.Kadir/Desktop/Panda Data/pythonProject1/TEST Backup.csv",encoding= 'latin-1')

    st.dataframe(df)

    st.subheader('Database names')
    st.write('1) employeeInformation\n2) employeeEducation\n3) employeeExperience\n4) TransactionTimestamps')

    st.write('---')


    x = st.text_input('What Database do you wish to see?')
    get_database_table(x)

    user_email = st.text_input("What is Your email?")
    if st.button("Checker"):
        email_list = df['email'].to_list() # MAKE SURE ITS A LIST SHERMAN!!
        if user_email in email_list:
            match = df[df['email'] == user_email]
            st.success(f"Its in here and the Name of this email is {match['employee_name'].values[0]}")



        else:
            st.warning("Sorry its not here")
    email = st.text_input(f":green[Email]", value=match['employee_name'].values[0])
    st.write(email)

Display()

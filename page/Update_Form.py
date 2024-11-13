import sqlite3

import numpy as np
import streamlit as st
import pandas as pd
from streamlit import date_input


def update_form_page(match):
    languages = [
        "English", "Spanish", "Mandarin", "Hindi", "Arabic", "Portuguese", "Bengali",
        "Russian", "Japanese", "Punjabi", "German", "Javanese", "Wu (Shanghainese)",
        "Malay/Indonesian", "Telugu", "Vietnamese", "Korean", "French", "Marathi",
        "Tamil", "Urdu", "Turkish", "Italian", "Yue (Cantonese)", "Thai", "Gujarati",
        "Jin", "Southern Min", "Persian", "Polish", "Pashto", "Kannada", "Xiang",
        "Malayalam", "Sundanese", "Hausa", "Odia", "Burmese", "Hakka", "Ukrainian",
        "Bhojpuri", "Tagalog", "Yoruba", "Maithili", "Uzbek", "Sindhi", "Amharic",
        "Fula", "Romanian", "Oromo", "Igbo", "Azerbaijani", "Awadhi", "Dutch",
        "Kurdish", "Serbo-Croatian", "Malagasy", "Saraiki", "Nepali", "Sinhalese",
        "Chittagonian", "Zhuang", "Khmer", "Turkmen", "Assamese", "Madurese",
        "Somali", "Marwari", "Magahi", "Haryanvi", "Hungarian", "Chhattisgarhi",
        "Greek", "Chewa", "Deccan", "Akan", "Kazakh", "Northern Min", "Sylheti",
        "Zulu", "Czech", "Kinyarwanda", "Dhundhari", "Haitian Creole", "Eastern Min",
        "Ilocano", "Quechua", "Kirundi", "Swedish", "Hmong", "Shona", "Uyghur",
        "Hiligaynon/Ilonggo", "Mossi", "Xhosa", "Belarusian", "Balochi", "Konkani","Filipino"
    ]
    countries = [
        "","Afghanistan", "Armenia", "Azerbaijan", "Bangladesh", "Bhutan", "Brunei", "Cambodia", "China",
        "Georgia", "India", "Indonesia", "Japan", "Kazakhstan", "Kyrgyzstan", "Laos", "Malaysia",
        "Maldives", "Mongolia", "Myanmar (Burma)", "Nepal", "North Korea", "Pakistan", "Philippines",
        "Singapore", "South Korea", "Sri Lanka", "Taiwan", "Tajikistan", "Thailand", "Timor-Leste (East Timor)",
        "Turkmenistan", "Uzbekistan", "Vietnam", "Cyprus", "Egypt", "Iran", "Iraq", "Jordan", "Lebanon",
        "Palestine", "Qatar", "Saudi Arabia", "Syria", "Turkey", "United Arab Emirates", "Yemen",
        "Canada", "United States", "Mexico", "Guatemala", "Belize", "Honduras", "El Salvador",
        "Nicaragua", "Costa Rica", "Panama", "Cuba", "Jamaica", "Haiti", "Dominican Republic",
        "Bahamas", "Barbados", "Saint Lucia", "Saint Vincent and the Grenadines", "Grenada",
        "Trinidad and Tobago", "Colombia", "Venezuela", "Guyana", "Suriname", "Brazil", "Peru",
        "Ecuador", "Bolivia", "Paraguay", "Chile", "Argentina", "Uruguay", "Algeria", "Libya",
        "Mauritania", "Morocco", "Sudan", "Tunisia", "Angola", "Botswana", "Eswatini (Swaziland)",
        "Lesotho", "Malawi", "Mozambique", "Namibia", "South Africa", "Zambia", "Zimbabwe",
        "Australia", "New Zealand", "Papua New Guinea", "Federated States of Micronesia", "Palau",
        "Marshall Islands", "Nauru", "Kiribati", "Tuvalu", "Samoa", "Tonga", "Tuvalu", "Fiji",
        "Solomon Islands", "Vanuatu", "New Caledonia", "French Polynesia", "Albania", "Andorra",
        "Armenia", "Austria", "Azerbaijan", "Belarus", "Belgium", "Bosnia and Herzegovina",
        "Bulgaria", "Croatia", "Cyprus", "Czech Republic", "Denmark", "Estonia", "Finland",
        "France", "Georgia", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy",
        "Kazakhstan", "Kosovo", "Latvia", "Liechtenstein", "Lithuania", "Luxembourg", "Malta",
        "Moldova", "Monaco", "Montenegro", "Netherlands", "North Macedonia", "Norway", "Poland",
        "Portugal", "Romania", "Russia", "San Marino", "Serbia", "Slovakia", "Slovenia", "Spain",
        "Sweden", "Switzerland", "Ukraine", "United Kingdom", "Vatican City", "Uganda", "Ethiopia",
        "Oman", "Kuwait", "Tanzania", "Ethiopia", "Côte d‘Ivoire","Somalia"
    ]

    def clean_languages_input(languages_str):
        # Convert to lowercase and remove extra words
        languages_str = languages_str.lower().replace(" and ", ", ").replace("/",", ").replace("/ ",", ").replace("& ",", ").replace("&",", ")
        # Split the string into a list of languages
        languages_list = [lang.strip().capitalize() for lang in languages_str.split(",")]
        cleared_languages = [lang for lang in languages_list if lang in languages]
        return cleared_languages

    def post_graduates():
        # THIS BAD BOY GETS ME THE INDEX BABY!! and I can use it in my countries list
        try:
            selected_index = countries.index(match['education_country_1'].values[0])
        except ValueError:
            selected_index = 0

        education_name_of_institution1 = st.text_area("Latest Education Accomplishment (Post_Grad/Masters/Bachelors/Diploma)", placeholder="Ex: PhD in Philosophy from XXXX",value=match['education_name_of_institution_1'].values[0])

        col1, col2 = st.columns(2)
        education_country_1 = col1.selectbox("1- Country of Graduation", countries,index=selected_index)
        education_date_1 = col2.text_input("1- Date of Graduation",value=match['education_date_1'].values[0])
        st.markdown("---")


    def masters():
        try:
            selected_index = countries.index(match['education_country_2'].values[0])
        except ValueError:
            selected_index = 0

        education_name_of_institution2 = st.text_area("Second Education Accomplishment", placeholder="Ex: Masters in Project Management from XXXX",value=match['education_name_of_institution_2'].values[0] or np.nan)

        col1, col2 = st.columns(2)
        education_country_2 = col1.selectbox("2- Country of Graduation", countries,index=selected_index)
        education_date_2 = col2.text_input("2- Date of Graduation",value=match['education_date_2'].values[0])
        st.markdown("---")


    def high_school_or_bachelors():
        try:
            selected_index = countries.index(match['education_country_2'].values[0])
        except ValueError:
            selected_index = 0

        education_name_of_institution3 = st.text_area("Last Education Accomplishment", placeholder="Ex: Diploma in Civil Engineering from XXXX",value=match['education_name_of_institution_3'].values[0])
        col1, col2 = st.columns(2)

        education_country_3 = col1.selectbox("3- Country of Graduation", countries,index=selected_index)
        education_date_3 = col2.text_input("3- Date of Graduation",value=match['education_date_3'].values[0])

    def employer_experience(number,match):
        try:
            selected_index = countries.index(match[f'country_{number}'].values[0])
        except ValueError:
            selected_index = 0

        col1, col2 = st.columns(2)
        previous_employer = col1.text_input(f'{number}- Company Name', key=f'company_name_{number}',value=match[f'employer_{number}'].values[0])
        previous_position = col2.text_input(f'{number}- Previous Position', key=f'previous_position_{number}',value=match[f'pos_{number}'].values[0])

        col1, col2, col3 = st.columns(3)
        from_date = col1.text_input(f'{number}- Starting Date?', key=f'starting_date_{number}',value=match[f'from_{number}'].values[0])
        previous_country = col2.selectbox(f"{number}- Which Country", countries, key=f'previous_country_{number}',index=selected_index)
        to_date = col3.text_input(f'{number}- Ending Date?', key=f'ending_date_{number}',value=match[f'to_{number}'].values[0])
        previous_project = st.text_area(f"{number}- Projects You've Done", key=f'projects_{number}',value=match[f'project_{number}'].values[0])
        duties = st.text_area(f"{number}- What Were Your Duties?", key=f'duties_{number}',value=match[f'project_{number}'].values[0])

    # Initialize session state for employer experience count
    if 'employer_experience_count' not in st.session_state:
        st.session_state.employer_experience_count = 1

    # Title
    st.markdown("<h1 style='text-align: center; color: grey;'>Update Form</h1>", unsafe_allow_html=True)
    # Sub Header
    st.markdown("Please :green[Check] and :blue[Update] the information below to finish the process")
    # Tabs
    Employee_Information, Employee_Education, Employee_Experience, Transaction_TimeStamps = st.tabs(['Employee Information', 'Employee Education', 'Employee Experience', 'Transaction TimeStamps'])

    with Employee_Information:
        with st.form("employee_information_form"):
            col1, col2 = st.columns(2)
            employee_name = col1.text_input('Employee Name',value=match['employee_name'].values[0])
            position = col2.text_input('Position',value=match['position'].values[0])
            col1, col2 = st.columns(2)
            telephone = col1.text_input("Enter your phone number",value=match['telephone'].values[0], max_chars=15, placeholder=" +971-501234567")
            email = col2.text_input("Enter Your Email",match['email'].values[0], placeholder="example123@mail.com")

            col1, col2, col3 = st.columns(3)
            years_of_exp = col1.number_input('Years of Experience',value= float(match['years_of_experience'].values[0]))
            regional_years_of_exp = col2.number_input('Regional Years of Experience',value=float(match['regional_years_of_experience'].values[0]))
            years_of_dorsch = col3.number_input('Years of Dorsch',value=float(match['years_with_dorsch'].values[0]))

            col1, col2, col3 = st.columns(3)
            nationality = col1.text_input('What is your Nationality?',value=match['nationality'].values[0])
            dob = col2.text_input('Date Of Birth',value=match['dob'].values[0] or np.nan,placeholder="DD/MM/YYYY")
            if match["marital_status"].values[0]== "Single":
                marital_status = col3.selectbox('What is your Marital Status?', ['Single', 'Married', 'Prefer not to Mention'],index=0)
            elif match["marital_status"].values[0]== "Single":
                marital_status = col3.selectbox('What is your Marital Status?', ['Single', 'Married', 'Prefer not to Mention'],index=1)
            else:
                marital_status = col3.selectbox('What is your Marital Status?', ['Single', 'Married', 'Prefer not to Mention'],index=2)

            col1, col2 = st.columns(2)

            if match['driving_license'].values[0] == "No":
                driving_license = col2.radio("Do you have a Driver's License?", ['Yes', 'No'],index=1)
            else:
                driving_license = col2.radio("Do you have a Driver's License?", ['Yes', 'No'],index=0)

            employee_languages = col1.multiselect('What Languages Do You Speak?', languages,default=clean_languages_input(match['languages'].values[0]))

            submit_employee_information = st.form_submit_button("Update")
            # Handle form submission
        if submit_employee_information:
            st.write("Form submitted!")
            st.write(f"Employee Name: :blue[{employee_name}]")
            st.write(f"Position: :blue[{position}]")
            st.write(f"Phone Number: :blue[{telephone}]")
            st.write(f"Email: :blue[{email}]")
            st.write(f"Years of Experience: :blue[{years_of_exp}]")
            st.write(f"Regional Years of Experience: :blue[{regional_years_of_exp}]")
            st.write(f"Years at Dorsch: :blue[{years_of_dorsch}]")
            st.write(f"Nationality: :blue[{nationality}]")
            st.write(f"Date of Birth: :blue[{dob}]")
            st.write(f"Marital Status: :blue[{marital_status}]")
            st.write(f"Driver's License: :blue[{driving_license}]")
            st.write(f"Languages Spoken: :blue[{', '.join(employee_languages)}]")

    with Employee_Education:
            st.subheader(":green[Education]")

            if not match['education_name_of_institution_3'].values[0] and not match['education_name_of_institution_2'].values[0]:
                post_graduates()
            elif not match['education_name_of_institution_3'].values[0]:
                post_graduates()
                master()
            else:
                post_graduates()
                masters()
                high_school_or_bachelors()







            st.markdown("---")
            st.subheader(":green[Professional Development]")
            membership = st.text_area('Memberships',value= match['memberships'].values[0])
            key_qualifications = st.text_area('Key Qualifications',value=match['key_qualifications'].values[0])
            professional_training = st.text_area('Professional Training',value=match['professional_training'].values[0])

    with Employee_Experience:
        current_employer_name = st.text_input("Name of Current Company",value=match['name_current_employer'].values[0])
        current_address = st.text_input("Address of Current Company",value=match['address_current_employer'].values[0])
        current_years = st.text_input("How Many Years Currently?", value=match['year_current'].values[0])
        current_job_title = st.text_input("What is Your Current Job Title?",value=match['job_title'].values[0])

        st.markdown("---")
        st.subheader("Previous Experience (Leave Empty If None)")

        # Button to add more employer experience sections
        if st.button("➕ Another Previous Employer?"):
            if st.session_state.employer_experience_count < 20:
                st.session_state.employer_experience_count += 1

        # Loop to display employer experience sections
        for i in range(1, st.session_state.employer_experience_count + 1):
            employer_experience(i,match)
            st.markdown("---")

    with Transaction_TimeStamps:
        st.markdown("<h2 style='text-align: center; color: teal'>Did it work?🙅‍♂️</h2>",unsafe_allow_html= True)
        st.subheader("Howdy :green[Parther]")
        with st.expander("Expand"):
            st.write("please close")
    # Example of accessing the stored values

    if st.button("Submit"):
        for i in range(1, st.session_state.employer_experience_count + 1):
            company_name = st.session_state.get(f'company_name_{i}', '')
            previous_position = st.session_state.get(f'previous_position_{i}', '')
            starting_date = st.session_state.get(f'starting_date_{i}', '')
            previous_country = st.session_state.get(f'previous_country_{i}', '')
            ending_date = st.session_state.get(f'ending_date_{i}', '')
            projects = st.session_state.get(f'projects_{i}', '')
            duties = st.session_state.get(f'duties_{i}', '')

            st.write(f"Employer {i}:")
            st.write(f"Company Name: {company_name}")
            st.write(f"Previous Position: {previous_position}")
            st.write(f"Starting Date: {starting_date}")
            st.write(f"Country: {previous_country}")
            st.write(f"Ending Date: {ending_date}")
            st.write(f"Projects: {projects}")
            st.write(f"Duties: {duties}")
            st.markdown("---")




df = pd.read_csv("C:/Users/Sharmarke.Kadir/Desktop/Panda Data/pythonProject1/TEST Backup.csv",encoding= 'latin-1')

#bsurio@ymail.com
#abrarahmed19@gmail.com
#Mudassirahmed10@gmail.com
email_checker = "Mudassirahmed10@gmail.com"
match = df[df['email']== email_checker]
update_form_page(match)
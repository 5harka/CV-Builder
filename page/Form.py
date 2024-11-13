import sqlite3
import streamlit as st
import pandas as pd


def form_page():
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
        "Afghanistan", "Armenia", "Azerbaijan", "Bangladesh", "Bhutan", "Brunei", "Cambodia", "China",
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

    def post_graduates():
        education_name_of_institution1 = st.text_area("Post-Graduate", placeholder="Ex: PhD in Philosophy from XXXX")
        col1, col2 = st.columns(2)
        phd_graduation_country = col1.selectbox("Country of Graduation (PhD)", countries)
        phd_graduation_date = col2.date_input("Date of Graduation (PhD)")
        st.markdown("---")
        masters()

    def masters():
        education_name_of_institution2 = st.text_area("Masters", placeholder="Ex: Masters in Project Management from XXXX")
        col1, col2 = st.columns(2)
        masters_graduation_country = col1.selectbox("Country of Graduation (Masters)", countries)
        masters_graduation_date = col2.date_input("Date of Graduation (Masters)")
        st.markdown("---")
        high_school_or_bachelors()

    def high_school_or_bachelors():
        education_name_of_institution3 = st.text_area("Bachelors / Diploma", placeholder="Ex: Diploma in Civil Engineering from XXXX")
        col1, col2 = st.columns(2)
        bachelors_graduation_country = col1.selectbox("Country of Graduation", countries)
        bachelors_graduation_date = col2.date_input("Date of Graduation")

    def employer_experience(number):
        col1, col2 = st.columns(2)
        previous_employer = col1.text_input(f'{number}- Company Name', key=f'company_name_{number}')
        previous_position = col2.text_input(f'{number}- Previous Position', key=f'previous_position_{number}')

        col1, col2, col3 = st.columns(3)
        from_date = col1.number_input(f'{number}- Starting Date?', step=1, key=f'starting_date_{number}')
        previous_country = col2.selectbox(f"{number}- Which Country", countries, key=f'previous_country_{number}')
        to_date = col3.number_input(f'{number}- Ending Date?', step=1, key=f'ending_date_{number}')
        previous_project = st.text_area(f"{number}- Projects You've Done", key=f'projects_{number}')
        duties = st.text_area(f"{number}- What Were Your Duties?", key=f'duties_{number}')

    # Initialize session state for employer experience count
    if 'employer_experience_count' not in st.session_state:
        st.session_state.employer_experience_count = 1

    # Title
    st.markdown("<h1 style='text-align: center; color: grey;'>Welcome to the Formpage</h1>", unsafe_allow_html=True)
    # Sub Header
    st.markdown("Please fill in the information below to start the process")
    resumeUploaded = st.file_uploader("Please Upload a pdf of Your CV")
    st.write(resumeUploaded)

    Employee_Information, Employee_Education, Employee_Experience, Transaction_TimeStamps = st.tabs(['Employee Information', 'Employee Education', 'Employee Experience', 'Transaction TimeStamps'])

    with Employee_Information:
        with st.form("employee_information_form"):
            col1, col2 = st.columns(2)
            employee_name = col1.text_input('Employee Name')
            position = col2.text_input('Position')
            col1, col2 = st.columns(2)
            telephone = col1.text_input("Enter your phone number", max_chars=15, placeholder=" +971-501234567")
            email = col2.text_input("Enter Your Email", placeholder="example123@mail.com")

            col1, col2, col3 = st.columns(3)
            years_of_exp = col1.number_input('Years of Experience', step=1)
            regional_years_of_exp = col2.number_input('Regional Years of Experience', step=1)
            years_of_dorsch = col3.number_input('Years of Dorsch', step=1)

            col1, col2, col3 = st.columns(3)
            nationality = col1.text_input('What is your Nationality?')
            dob = col2.date_input('Date Of Birth')
            marital_status = col3.selectbox('What is your Marital Status?', ['Single', 'Married', 'Prefer not to Mention'])

            col1, col2 = st.columns(2)
            driving_license = col2.radio("Do you have a Driver's License?", ['Yes', 'No'])
            employee_languages = col1.multiselect('What Languages Do You Speak?', languages)

            submit_employee_information = st.form_submit_button("Save")
            # Handle form submission
        if submit_employee_information:
            st.write("Form submitted!")
            st.write(f"Employee Name: :blue[{employee_name}]")
            st.write(f"Position: {position}")
            st.write(f"Phone Number: {telephone}")
            st.write(f"Email: {email}")
            st.write(f"Years of Experience: {years_of_exp}")
            st.write(f"Regional Years of Experience: {regional_years_of_exp}")
            st.write(f"Years at Dorsch: {years_of_dorsch}")
            st.write(f"Nationality: {nationality}")
            st.write(f"Date of Birth: {dob}")
            st.write(f"Marital Status: {marital_status}")
            st.write(f"Driver's License: {driving_license}")
            st.write(f"Languages Spoken: {', '.join(employee_languages)}")

    with Employee_Education:
            st.subheader("Education")
            education_level = st.selectbox("What level is Your Education?", ['', 'Post-Graduate', 'Masters', 'Bachelors', 'Diploma'])

            if education_level == 'Post-Graduate':
                post_graduates()
            elif education_level == 'Masters':
                masters()
            elif education_level in ['Bachelors', 'Diploma']:
                high_school_or_bachelors()

            st.markdown("---")
            st.subheader("Professional Development")
            membership = st.text_area('Memberships')
            key_qualifications = st.text_area('Key Qualifications')
            professional_training = st.text_area('Professional Training')


    with Employee_Experience:
        current_employer_name = st.text_input("Name of Current Company")
        current_address = st.text_input("Address of Current Company")
        current_years = st.number_input("How Many Years Currently?", step=1)
        current_job_title = st.text_input("What is Your Current Job Title?")

        st.markdown("---")
        st.subheader("Previous Experience (Leave Empty If None)")

        # Button to add more employer experience sections
        if st.button("➕ Another Previous Employer?"):
            if st.session_state.employer_experience_count < 20:
                st.session_state.employer_experience_count += 1

        # Loop to display employer experience sections
        for i in range(1, st.session_state.employer_experience_count + 1):
            employer_experience(i)
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


form_page()



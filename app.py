import streamlit as st
import pandas as pd

st.sidebar.title('Navigation')
section = st.sidebar.radio('Go To', ['About', 'skills', 'Experience', 'Education', 'Contact'])

skills = {
    'python': 0.8,
    'Machine Learning': 0.8,
    'Streamlit': 0.9,
    'SQL': 0.7,
    'Data Visualization': 0.8
}

st.title('Employee Name: Ryan')
st.subheader('Data Scientist')

if section == 'About':
    st.markdown(f"""
    Experienced data scientist
    with strong skills in analytics, 
    machine learning, and storytelling with data. 
    Passionate about turning data into actionable insights.
    """)

elif section == 'skills':
    st.header('Sills Overview')
    for skill, level in skills.items():
        st.write(f'{skill}')
        st.progress(level)
    df_skills = pd.DataFrame({
        'Skill': list(skills.keys()),
        'Proficiency': list(skills.values())
    })
    st.bar_chart(df_skills.set_index('Skill'))

elif section == 'Experience':
    st.header('Work Experiance')

    with st.expander(f'Data Scientist | COMPANY | June 2023'):
        st.write(f"""
          - Built 5 streamlit apps in production
          - Built 30+ Dashboards for risk and underwriting
          - Developed 20 DBT Models
                """)

    with st.expander(f'You Tuber | Ryan & Matt DS | April 2023'):
            st.write(f"""
              - Created Over 200 Data Videos
              - Full Python Pandas Course
              - Full Scikit learn course
                    """)

    with st.expander(f'Data Analyst | Tax softwar Company | April 2021'):
                st.write(f"""
                  - Worked with Exec team on software pricing and sales
                  - Looked over fraud and risk concerns with legal
                        """)

elif section == 'Education':
    st.header('Education')
    st.write('B.s. In Electrical Engineering University of Central of FL 2020')

elif section == 'Contact':
    st.header('Get in touch')
    col1, col2 = st.columns(2)
    with col1:
         email = st.text_input('Email')
         phone = st.text_input('Phone')
    with col2:
         linkedin = st.text_input('LinkedIN URL')
         Discord = st.text_input('Discord Name')

    message = st.text_area('Message')

    if st.button('Send'):
         st.success("Thanks for reaching out, I'll be in contact soon")

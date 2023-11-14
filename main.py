import streamlit as st
import pandas


container = st.container()

with container:
    col1, col2 = st.columns(2)

    with col1:
        st.image('images/my_photo.jpeg')

    with col2:
        st.title('Olena Abert')
        content = """Front-end developer with experience in maintaining and building web pages. 
        Proficient with HTML/CSS/SCSS/JS/TypeScript, ReactJS (Redux, Redux Toolkit) and Python. 
        Building state-of-the-art, easy to use, user-friendly websites and applications is truly a passion of mine. 
        In addition to my knowledge base, I actively seek out new technologies and stay up-to-date on industry trends and
         advancements."""
        st.info(content)

sub_content = """Below you can find some of the apps I have build in Python."""
st.write(sub_content)
col3, col4 = st.columns(2)

data_frame = pandas.read_csv('data.csv', sep=';')

with col3:
    for index, row in data_frame[:10].iterrows():
        st.header(row['title'])

with (col4
      ):
    for index, row in data_frame[10:].iterrows():
        st.header(row['title'])


import streamlit as st

st.set_page_config(page_title="My App", layout="wide")

home_page = st.Page('home.py', title='Home', default=True)
analysis_page = st.Page('analysis.py', title='Analysis')


nav = st.navigation([home_page, analysis_page], position='hidden')
nav.run()

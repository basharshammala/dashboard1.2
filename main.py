import streamlit as st

home_page =  st.Page('home.py',title='Home', default=True)
analysis_page = st.Page('analysis.py', title='Analysis')

nav =  st.navigation([home_page, analysis_page], position='hidden')
nav.run()
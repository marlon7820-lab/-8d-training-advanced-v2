# streamlit_app.py - wrapper to run the main app file

try:
    import app_advanced_v2  # this will execute your full app
except Exception as e:
    import streamlit as st
    st.title("Error loading app_advanced_v2.py")
    st.write(e)

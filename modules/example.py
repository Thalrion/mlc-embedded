import streamlit as st

def show_app():
    st.write("Test App")

    with st.sidebar:
        st.write("Test")
        full_screen=st.toggle("Show something", value=False)
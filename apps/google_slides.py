import streamlit as st
from streamlit.components.v1 import iframe as st_iframe

default_url = "https://docs.google.com/presentation/d/1AkfSZiTULjeq7_5y5pY-EdDcfO6NIvBf9i9ieMhRF7E/embed"


with st.sidebar:
    st.header("Google Slides")
    url_container = st.container()
    hide_controls = st.checkbox("Hide controls", value=True)
    default_url = f"{default_url}?rm=minimal" if hide_controls else default_url
    url = url_container.text_area("URL", value=default_url, height=150)


st_iframe(default_url, height=600)

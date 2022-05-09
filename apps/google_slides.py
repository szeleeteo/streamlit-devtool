import streamlit as st

default_url = "https://docs.google.com/presentation/d/1AkfSZiTULjeq7_5y5pY-EdDcfO6NIvBf9i9ieMhRF7E/embed"

with st.sidebar:
    st.header("Google Slides")
    url_container = st.container()
    hide_controls = st.checkbox("Hide controls", value=True)
    loop = st.checkbox("Loop after the last slide", value=True)
    default_url = f"{default_url}?rm=minimal" if hide_controls else default_url
    default_url = f"{default_url}?loop=true" if loop else default_url
    url = url_container.text_area("URL", value=default_url, height=150)


st.components.v1.iframe(default_url, height=600)

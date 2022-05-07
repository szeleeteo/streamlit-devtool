import pkgutil
import runpy

import streamlit as st

import apps

apps_module = {
    module.name.replace("_", " ").title(): f"{apps.__package__}.{module.name}"
    for module in pkgutil.iter_modules(["apps"])
    if not module.ispkg
}


def main():
    st.set_page_config(
        page_title="Handy DevTools - Streamlit",
        page_icon="🛠",
        layout="wide",
        initial_sidebar_state="collapsed",
        menu_items={
            "About": f"Source code: https://github.com/szeleeteo/streamlit-devtool"
        },
    )
    st.sidebar.title("Apps")
    choice = st.sidebar.selectbox("Select an app", list(apps_module.keys()))
    runpy.run_module(apps_module[choice], run_name="__main__")


if __name__ == "__main__":
    main()

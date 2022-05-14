[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/szeleeteo/streamlit-devtool)

# Setup
# Pre-requisites:
    - Python 3.8
    - Makefile (optional)

# Setup with Makefile
1. For local development with full depdencies installed, run `make dev` (virtualenv is auto created)
1. For minimal dependencies (e.g. without Jupyter notebook, formatter etc), run `make release` instead
1. To run the main app, run `make run`

# Setup without Makefile
1. Create a new virtual environment with `python -m venv venv`
1. Activate virtualenv with `source venv/bin/activate`
1. For local development with full dependencies installed, run `pip install -r requirements-dev.txt`
1. For minimal dependencies (e.g. without Jupyter notebook, formatter etc), run `pip install -r requirements.txt`
1. To run the main app, run `streamlit run streamlit_app.py`

# Run individual script
1. If virtual env is activated, run individual streamlit script with `streamlit run <python script path relative to root directory>`
1. Otherwise, this will also work `venv/bin/streamlit run <python script path relative to root directory>`


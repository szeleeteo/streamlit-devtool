.PHONY: dev run clean
.DEFAULT: help

help: ## Display this help message
	@echo "Please use \`make <target>\` where <target> is one of"
	@awk -F ':.*?## ' '/^[a-zA-Z]/ && NF==2 {printf "\033[36m  %-25s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

clean: ## Remove general artifact files
	find . -name '.coverage' -delete
	find . -name '*.pyc' -delete
	find . -name '*.pyo' -delete
	find . -name '.pytest_cache' -type d | xargs rm -rf
	find . -name '__pycache__' -type d | xargs rm -rf
	find . -name '.ipynb_checkpoints' -type d | xargs rm -rf

venv: ## Create virtual environment if venv directory not present
	`which python3.8` -m venv venv
	venv/bin/pip install -U pip wheel --no-cache-dir

dev: venv requirements-dev.txt ## Install dependencies for dev
	venv/bin/pip install -r requirements-dev.txt

release: venv requirements.txt ## Install dependencies for release (Streamlit Cloud)
	venv/bin/pip install -r requirements.txt

nbextension: ## Install Jupyter Notebook extensions
	venv/bin/jupyter contrib nbextension install

nb: ## Run Jupyter Notebook
	venv/bin/jupyter notebook 

lab: ## Run Jupyter Lab 
	venv/bin/jupyter lab

run: ## Run with dev dependencies
	venv/bin/python -m streamlit run streamlit_app.py

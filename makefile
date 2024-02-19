init: purge
	python -m venv env
	env/bin/pip install --upgrade pip wheel setuptools
	env/bin/pip install .
	env/bin/pip install -r dev_requirements.txt

clear:
	-@rm -rf MANIFEST
	-@rm -rf annotations
	-@rm -rf .pytest_cache tests/__pycache__ __pycache__ _skbuild dist .coverage build
	-@find . -type d -name '*.egg-info' | xargs rm -r
	-@find . -type d -name '*.ipynb_checkpoints' | xargs rm -r
	-@find . -type f -name '*.pyc' | xargs rm -r
	-@find . -type f -name '*.zip' | xargs rm -r


rebuild:
	env/bin/pip uninstall -y keepdb
	env/bin/pip install .

purge: clear
	-@rm -rf env

test:
	env/bin/pytest

lint:
	env/bin/ruff src/ tests/

fix:
	env/bin/ruff src/ tests/ --fix

lab:
	env/bin/jupyter lab

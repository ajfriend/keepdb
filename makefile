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
	-@find . -type f -name '*.pyc' | xargs rm -r
	-@find . -type d -name '*.ipynb_checkpoints' | xargs rm -r

purge: clear
	-@rm -rf env


lint:
	env/bin/ruff .

fix:
	env/bin/ruff . --fix

lab:
	env/bin/jupyter lab
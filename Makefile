# python version used to bootstrap local development environment
PYTHON_VERSION=3.9.6
PROJECT_NAME=dockerfile-recover

# create virtual environment using pyenv
create-venv:
	# install target python version if it does not exist
	pyenv install --skip-existing ${PYTHON_VERSION}
	# create virtual environment
	pyenv virtualenv --force ${PYTHON_VERSION} ${PROJECT_NAME}
	# automatically activate virtual environment
	pyenv local ${PROJECT_NAME}

# remove all installed packages from active virtual environment
clean:
	pip freeze | cut -d ' ' -f1 | xargs --no-run-if-empty pip uninstall -y

# install project dependencies
install:
	# use latest pip
	python -m pip install --upgrade pip
	# use poetry for dependency management
	poetry install

# export dependencies for external build process
lock:
	# ensure lock file is up to date
	poetry lock
	# export hashed requirements to simplify external build processes
	poetry export --dev --output requirements-dev.txt
	poetry export --output requirements-container.txt

# run tests
test:
	pytest

coverage:
	coverage run -m pytest
	coverage report --fail-under=100

# lint code
lint:
	# sort import statements
	isort .
	# format code with black
	black .
	# run static type checker
	mypy dockerfile_recover tests --ignore-missing-imports
	# run static code analysis
	pylint dockerfile_recover tests

# check linting without changing source files
check-lint:
	# check imports
	isort --check-only .
	# check code formatting
	black --check .

# build and test the entire project
build: lock install lint coverage

# install poetry
get-poetry:
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

# Manage Conf

<a href="https://github.com/ambv/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

**WIP**

## Install

Requires [Poetry](https://poetry.eustace.io).

```bash
# create a Python3 virtual environment
virtualenv -p python3 env

# activate the virtual env
source env/bin/activate

# install requirements
poetry install
```

## Tests

```bash
# run tests
pytest -vv

# coverage report
pytest --cov=manage_conf tests/
```

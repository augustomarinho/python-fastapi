<div align="center">
<h1>FastAPI Hexagonal Architecture</h1>
<div>
    <img src="https://img.shields.io/badge/FastAPI-Python%203.11-blue.svg" alt="FastAPI supports Python 3.11"/>    
    <a href="https://python-poetry.org/"><img src="https://img.shields.io/badge/maintained%20with-poetry-rgb(30%2041%2059).svg" alt="poetry"/></a>
</div>
</div>

<p>This project was created to study the concepts of the Hexagonal Architecture using Python and FastAPI.</p>
<br>

* [Init](#init)
* [Entry in project dir](#entry-in-project-dir)
* [Create environment](#create-environment)
* [Install dependencies](#install-dependencies)
* [Start](#start)
* [Run Test](#run-test)
* [Run Lint](#run-lint)
* [Alembic](#alembic)
* [Alembic Migrations](#alembic-migrations)


# Init
 * Install pyenv: https://github.com/pyenv/pyenv#installation
 * Install Docker: https://docs.docker.com/get-docker/
 * Install Poetry: https://python-poetry.org/docs/#installation

# Entry in project dir
```bash
cd python-fastapi
```

# Create environment
```bash
pyenv install 3.11.0
pyenv virtualenv 3.11.0 python-fastapi
pyenv activate python-fastapi
```

# Install dependencies
```bash
poetry install
```

# Start
```bash
poetry run start
```

# Run Test
```bash
poetry run pytest -v
```

# Run Lint
```bash
poetry run black --check . && poetry run isort --check . && poetry run flake8 .
```

# Alembic
Alembic was initialize with the command:
```bash
poetry run alembic init infrastructure/alembic/migrations
```

# Alembic Migrations
Create migrations
```bash
poetry run alembic revision -m "create book table"
```

Execute migrations
```bash
poetry run alembic upgrade head
```

List migrations history
```bash
poetry run alembic history --verbose
```
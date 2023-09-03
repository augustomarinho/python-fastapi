# FastAPI Hexagonal Architecture

# Init
 Install pyenv https://github.com/pyenv/pyenv#installation

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

# Install dependecies
```bash
poetry install
```

# Start
```bash
poetry run start
```

# Run Test
```bash
poetry run test
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
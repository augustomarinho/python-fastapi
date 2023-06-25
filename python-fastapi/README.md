# FastAPI Clean Architecture

# Init
 Install pyenv https://github.com/pyenv/pyenv#installation

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
# FastAPI Application

A minimal FastAPI application template.

## Features

- FastAPI for API development
- pyproject.toml with setuptools as build system
- Ruff for linting
- UV for dependency management

## Setup

### Install dependencies

```bash
# Install uv if not already installed
curl -sSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv pip install -e .
```

### Development dependencies

```bash
uv pip install -e ".[dev]"
```

## Running the application

```bash
python run.py
```

With custom options:

```bash
# Change port
python run.py --port 8080

# Disable auto-reload
python run.py --no-reload

# Change host and port
python run.py --host 127.0.0.1 --port 5000
```

View all available options:

```bash
python run.py --help
```

Or directly with uvicorn:

```bash
uvicorn app.main:app --reload
```

## API Documentation

Once the application is running, you can access:

- API documentation: http://localhost:8080/docs
- Alternative documentation: http://localhost:8080/redoc

# FastAPI Application Template

A minimal FastAPI application template with a modern project structure.

## Features

- **FastAPI** for modern API development
- **Jinja2 Templates** for server-side rendering
- **Modern Project Structure** with src layout
- **Task-based Workflow** using Taskfile.yml
- **Code Quality Tools**: Ruff for formatting and linting
- **Dependency Management**: UV for fast package installation

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

The project uses [Task](https://taskfile.dev/) for common operations:

```bash
# Run with auto-reload for development
task run:dev

# Run without auto-reload for production
task run

# Run with custom options
task run:custom -- --host 127.0.0.1 --port 5000 --no-reload
```

If you prefer to run directly with Python:

```bash
python -m src.app.main
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

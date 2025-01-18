# WA-Bot-Template

[![CI/CD Pipeline](https://github.com/Kitsune-Studios/WA-Bot-Template/actions/workflows/ci.yml/badge.svg)](https://github.com/Kitsune-Studios/WA-Bot-Template/actions/workflows/ci.yml)


A WhatsApp bot template built with FastAPI and uv package manager, designed to be deployed with Docker.

## Features

- FastAPI-based REST API
- WhatsApp message handling
- Ngrok tunnel integration
- AWS Lambda compatible (via Mangum)
- Docker containerization
- Modern dependency management with uv

## Requirements

- Python 3.11+
- Docker (optional)
- uv package manager

## Dependencies

- boto3
- fastapi
- mangum
- ngrok
- nox
- pulumi
- requests

## Quick Start

Before you begin, ensure you have `uv` installed. You can install it using:

```bash
winget install --id=astral-sh.uv  -e # Windows
```

```bash
brew install uv # macOS
```

```bash
curl -fsSL https://deno.land/x/install/install.sh | sh # Linux
```

for more information about installation and shell autocomplete, please visit this [guide](https://docs.astral.sh/uv/getting-started/installation/).
### Local Development

1. Clone the repository
2. Install dependencies:
```bash
uv sync
```
3. Set up environment variables
4. Run the server:
```bash
uvicorn backend.main:app --reload
```

### Docker Deployment

Build and run using Docker:

```bash
docker build -t wa-bot .
docker run -p 80:80 wa-bot
```

## Development

For development, additional tools are available:
- pre-commit for git hooks and code formatting
- Ruff for linting and formatting
- Nox for automated testing and development tasks

### Pre-commit

Install pre-commit hooks:
```bash
pre-commit install
```

### Nox

Automated testing and development tasks are available using Nox. To run a session, use the following command:

```bash
nox -s [name] # Run specific session. e.g. nox -s format
```

#### Ruff

ruff is a tool for linting and formatting code. It is used in the `format` & `lint` session in Nox.
>to run the session, use the following command:

```bash
nox -s format # Format code
```

```bash
nox -s lint # Lint code
```

## License

MIT
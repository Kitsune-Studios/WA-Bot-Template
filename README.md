# WA-Bot-Template

[![CI/CD Pipeline](https://github.com/Kitsune-Studios/WA-Bot-Template/actions/workflows/ci.yml/badge.svg)](https://github.com/Kitsune-Studios/WA-Bot-Template/actions/workflows/ci.yml)

A WhatsApp bot template built with FastAPI and uv package manager, designed to be deployed with Docker.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Dependencies](#dependencies)
- [Quick Start](#quick-start)
  - [Local Development](#local-development)
    - [Pre-commit](#pre-commit-optional)
    - [Nox](#nox)
    - [Ruff](#ruff)
- [External References](#external-references)
- [License](#license)



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

for more information about UV installation and shell autocomplete, please visit this [guide](https://docs.astral.sh/uv/getting-started/installation/).
### Local Development

1. Clone the repository
```bash
git clone https://github.com/Kitsune-Studios/WA-Bot-Template.git
```
2. Install dependencies:
```bash
uv sync
```
3. Set up environment variables

```bash
cp .env.example .env
```

4. Run the server:
- Using local development server:
```bash
nox -s dev # Run the development server

```
- Using Docker:
```bash
nox -s docker # Build and run the Docker container
```
 >[!NOTE]
 > The server will be running on http://localhost:8000 by default on both methods.

For development, additional tools are available:
- pre-commit for git hooks and code formatting
- Ruff for linting and formatting
- Nox for automated testing and development tasks

#### Pre-commit (Optional)

 >[!TIP]
 > _it is recommended to install pre-commit hooks if you are contributing to the project_

Install pre-commit hooks: (requires pre-commit to be installed)
```bash
pre-commit install
```

#### Nox

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
## External References

Project files:
- [Dockerfile](./Dockerfile) - Container configuration
- [noxfile.py](./noxfile.py) - Development automation
- [pyproject.toml](./pyproject.toml) - Project dependencies and configuration
- [.pre-commit-config.yaml](./.pre-commit-config.yaml) - Git hooks configuration
- [backend/main.py](./backend/main.py) - Main application entry point

Documentation:
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [Docker Docs](https://docs.docker.com/)
- [uv Package Manager](https://github.com/astral-sh/uv)
- [Mangum](https://github.com/jordaneremieff/mangum)

## License

MIT
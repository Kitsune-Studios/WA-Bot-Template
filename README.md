# WA-Bot-Template
[![CI/CD Pipeline](https://github.com/Kitsune-Studios/WA-Bot-Template/actions/workflows/ci.yml/badge.svg)](https://github.com/Kitsune-Studios/WA-Bot-Template/actions/workflows/ci.yml)
A WhatsApp bot template built with FastAPI and uv package manager, designed to be deployed with Docker.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Dependencies](#dependencies)
- [Quick Start](#quick-start)
  - [Local Development](#local-development)
    - [Pre-commit (optional)](#pre-commit-optional)
    - [Nox](#nox)
    - [Ruff](#ruff)
- [Testing](#testing)
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
For more information about UV installation and shell autocomplete, please visit this [guide](https://docs.astral.sh/uv/getting-started/installation/).

1. Clone the repository
```bash
git clone https://github.com/Kitsune-Studios/WA-Bot-Template.git && cd $_ # Download and navigate to the project directory
```
2. Install dependencies:
```bash
uv sync --all-groups --dev # Install dependencies using uv
```
3. Set up environment variables
```bash
cp .env.example .env # Copy the example environment file. Edit the .env file with your credentials
```

### Local Development
4. Run the server:
- Using local development server:
```bash
nox -s dev # Run the development server
```
- Using Docker:
```bash
nox -s docker # Build and run the Docker container
```
> [!NOTE]
> The server will be running on http://localhost:8000 by default on both methods.

Happy coding! 🚀

**_For development, additional tools are available:_**
- pre-commit for git hooks and code formatting (optional)
- Ruff for linting and formatting code
- Nox for automated testing and development tasks

#### Pre-commit (Optional)
> [!IMPORTANT]
> _It is recommended to install pre-commit hooks if you are contributing to the project_

Install pre-commit hooks on the project:
```bash
pre-commit install --install-hooks # it will add the hooks to the git repository
```
> [!TIP]
> You can check more about pre-commit hooks [here](https://pre-commit.com/). Settings can be found in [.pre-commit-config.yaml](./.pre-commit-config.yaml)

### Scripts
Some out of the box scripts are available for development and testing:
```bash
uvx nox -s [name] # Run specific session. e.g. nox -s docker check available sessions using nox -l
```

#### Ruff
Ruff is a tool for linting and formatting code. It is used in the `format` & `lint` session in Nox.
> To run the session, use the following command:
```bash
uvx ruff check # Check code formatting
```
```bash
uvx ruff format # Format code
```

## Testing

To ensure the quality and functionality of the project, a comprehensive suite of tests is provided. The testing framework used in this project is `pytest`.

### Running Tests

1. Install the required dependencies for testing:
```bash
uv sync --all-groups --dev # Install all dependencies including dev dependencies
```
2. Run the tests:
```bash
nox -s tests # This will run all the tests using Nox
```

### Test Structure

- Unit tests are located in the `backend/tests` directory.
- Integration tests are located in the `backend/tests/integration` directory.

### Faker

The project uses `faker` for generating fake data during testing. This helps in creating realistic test cases and scenarios.

For more information on `faker`, you can visit the [Faker documentation](https://faker.readthedocs.io/en/master/).

## External References
Documentation:
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [Docker Docs](https://docs.docker.com/)
- [Astral](https://astral.sh/)
  - [uv](https://docs.astral.sh/uv/getting-started/installation/)
  - [ruff](https://docs.astral.sh/ruff/getting-started/installation/)
- [Mangum](https://github.com/jordaneremieff/mangum)
- [Pulumi](https://www.pulumi.com/)
  - [Pulumi AWS](https://www.pulumi.com/docs/reference/clouds/aws/)
  - [Pulumi GCP](https://www.pulumi.com/docs/reference/clouds/gcp/)
- [Ngrok](https://ngrok.com/) (soon to be deprecated)
- [Nox](https://nox.thea.codes/)

## License
This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

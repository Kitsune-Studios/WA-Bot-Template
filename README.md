# WA-Bot-Template

A WhatsApp bot template built with FastAPI and uv package manager, designed to be deployed with Docker.

## Features

- FastAPI-based REST API
- WhatsApp message handling
- Ngrok tunnel integration
- AWS Lambda compatible (via Mangum)
- Docker containerization
- Modern dependency management with uv

## Requirements

- Python 3.12+
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

### Local Development

1. Clone the repository
2. Install dependencies:
```bash
uv sync
```
3. Set up environment variables
4. Run the server:
```bash
uvicorn app.main:app --reload
```

### Docker Deployment

Build and run using Docker:

```bash
docker build -t wa-bot .
docker run -p 80:80 wa-bot
```

## Development

For development, additional tools are available:
- Ruff for linting and formatting
- Nox for automated testing and development tasks

Run development tasks with nox:
```bash
# Run all default sessions (format, lint, test)
nox

# Run specific session
nox -s test
```

## License

MIT
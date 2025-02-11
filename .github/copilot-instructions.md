# GitHub Copilot Instructions

This file contains instructions and context for GitHub Copilot to better assist with this Python/FastAPI/Docker project.

## Project Overview
- Python-based REST API using FastAPI framework
- Package management with `uv`
- Containerized with Docker
- Modern async web application

## Code Style Preferences
```python
# Example style conventions
async def function_name(param: str) -> dict:
    """
    Function docstring using Google style.

    Args:
        param: Parameter description

    Returns:
        dict: Return value description
    """
    pass
```

## Common Patterns
- Use async/await for database operations
- Type hints required for all functions
- Snake case for variables and functions
- Upper camelcase for class names
- Use f-strings for string formatting

## Dependencies
- Python 3.11+
- FastAPI
- uv (for package management)
- Docker
- Pydantic for data validation

## Testing Conventions
- pytest for unit tests
- async test cases with pytest-asyncio
- fixtures in conftest.py

## Docker Guidelines
- Multi-stage builds preferred
- Alpine-based images when possible
- Non-root user for production
- Environment variables for configuration

## Security Requirements
- Input validation with Pydantic
- CORS configuration required
- Dependencies with known vulnerabilities avoided
- Secrets handled via environment variables

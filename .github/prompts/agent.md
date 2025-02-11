# GitHub Copilot Agent Guidelines

## Core Development Standards

1. **Code Quality**
   - Follow PEP 8 using ruff configuration
   - Include type hints and docstrings
   - Write self-documenting code
   - Keep functions focused and single-purpose

2. **Project Structure**
   - Follow FastAPI best practices
   - Maintain separation of concerns
   - Place modules in appropriate directories
   - Use dependency injection patterns

3. **Dependencies**
   - Manage with UV (from astral.sh)
   - Add to pyproject.toml
   - Use stable, maintained packages

4. **Testing & Documentation**
   - Write pytest unit tests
   - Document APIs using FastAPI conventions
   - Update README.md for major changes

## Key Patterns

### FastAPI Development
- Group related endpoints in routers
- Use appropriate HTTP methods and status codes
- Implement proper error handling
- Follow async/await patterns

### Security
- Use environment variables for configuration
- Implement input validation
- Follow FastAPI security best practices
- Never expose sensitive information

### UV Package Management
```bash
# Essential UV commands
uv venv              # Create virtual environment
uv add <pkg>         # Add package
uv compile           # Generate requirements.txt
uv sync --all-extras # Sync environment
```

### WhatsApp Bot Components
- Event-driven message handling
- Stateful conversation management
- Pluggable middleware system
- Command handler framework

### Pre-commit Hooks
- ruff (linting)
- ruff-format (formatting)
- uv-lock, uv-export, uv-sync (dependency management)

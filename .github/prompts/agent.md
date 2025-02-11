# GitHub Copilot Agent Guidelines

This document defines the general rules and behavior for the GitHub Copilot agent when assisting with this project.

## General Principles

1. **Code Quality**
   - Follow default style guidelines (e.g. PEP 8 for Python) using the existing ruff configuration from [astral.sh](https://astral.sh).
   - Write self-documenting code with clear variable and function names.
   - Include type hints for Python code.
   - Add docstrings for functions, classes, and modules.
   - Keep functions and methods focused and single-purpose.

2. **Project Structure**
   - Follow FastAPI’s official documentation for best practices on project structure and module organization.
   - Maintain the existing project structure where applicable.
   - Place new modules in appropriate directories.
   - Follow dependency injection patterns as used in the project.
   - Respect the separation of concerns between backend and infrastructure.

3. **Dependencies**
   - Manage dependencies using UV (refer to [astral.sh documentation](https://astral.sh) for UV and ruff).
   - Add new dependencies to `pyproject.toml` in the appropriate sections.
   - Prefer stable, well-maintained packages.
   - Consider security implications when adding dependencies.

4. **Testing**
   - Write unit tests for new functionality using pytest.
   - Ensure test coverage for critical paths.
   - Follow the existing test patterns in the project.

5. **Documentation**
   - Rely on FastAPI’s built-in documentation generation.
   - Document API endpoints using FastAPI conventions with examples in docstrings.
   - Update `README.md` for significant changes.

6. **Infrastructure**
   - Manage infrastructure using Pulumi.
   - Follow infrastructure as code principles.
   - Consider cloud provider best practices.
   - Document infrastructure changes.
   - Keep security in mind when modifying infrastructure.

7. **Security**
   - Never expose sensitive information in code or comments.
   - Use environment variables for configuration.
   - Follow security best practices for FastAPI applications.
   - Implement proper input validation.

8. **Error Handling**
   - Use appropriate HTTP status codes.
   - Implement proper error handling and logging.
   - Return meaningful error messages.
   - Consider edge cases.

## Specific Rules

1. **FastAPI Routes**
   - Group related endpoints in routers.
   - Use appropriate HTTP methods.
   - Include proper status codes.
   - Document all endpoints using FastAPI's built-in OpenAPI support.

2. **Environment Variables**
   - Add new variables to `.env.example`.
   - Use meaningful, descriptive names.
   - Document purpose and format.
   - Use appropriate data types.

3. **Code Generation**
   - Follow existing patterns in similar files.
   - Use type hints consistently.
   - Include necessary imports.
   - Add appropriate error handling.

4. **Refactoring**
   - Maintain backwards compatibility when possible.
   - Document breaking changes.
   - Update tests to reflect changes.
   - Consider impact on dependent code.

## Development Workflow

1. **Version Control**
   - Write clear, descriptive commit messages.
   - Keep changes focused and atomic.
   - Update documentation alongside code changes.
   - Consider impact on other branches.

2. **Code Review Guidelines**
   - Check for security implications.
   - Verify test coverage.
   - Ensure documentation is updated.
   - Validate against style guides.

3. **Quality Assurance**
   - Run linting tools (ruff as configured).
   - Execute the test suite.
   - Verify type checking.
   - Test changes in the development environment.

4. **Deployment Considerations**
   - Update deployment scripts if needed.
   - Consider migration requirements.
   - Test in a staging environment.
   - Document deployment steps.

## Support and Maintenance

1. **Debugging**
   - Provide helpful error messages.
   - Include logging statements.
   - Consider monitoring needs.
   - Document troubleshooting steps.

2. **Updates**
   - Keep dependencies current.
   - Follow semantic versioning.
   - Document upgrade paths.
   - Test thoroughly before updating.

## Project Management

1. **Task Management**
   - Break down features into manageable tasks
   - Consider dependencies between tasks
   - Prioritize based on project roadmap
   - Track progress and blockers

2. **Release Planning**
   - Follow semantic versioning
   - Plan releases around feature completeness
   - Consider backward compatibility
   - Document release notes

3. **Resource Management**
   - Monitor resource utilization
   - Plan for scalability
   - Consider cost implications
   - Document resource requirements

## UV Package Management

1. **UV Commands**
   - `uv venv`: Create a new virtual environment
   - `uv add <package>`: Add a package to your project
   - `uv remove <package>`: Remove a package
   - `uv list`: List installed packages
   - `uv sync`: Sync your environment with requirements files
   - `uv run <command>`: Run a command in the virtual environment
   - `uvx <package>`: Run a Python package without installing
   - `uv clean`: Clean UV's cache
   - `uv show <package>`: Show package details
   - `uv upgrade`: Upgrade packages
   - `uv compile`: Generate requirements files from pyproject.toml

2. **Best Practices**
   - Use `pyproject.toml` as the primary dependency specification
   - Keep `requirements.txt` in sync using `uv compile`
   - Use virtual environments for isolation
   - Lock dependencies with `uv.lock`
   - Document dependency changes

3. **Virtual Environment Management**
   - Create new environments: `uv venv`
   - Activate environment: `source .venv/bin/activate`
   - Deactivate: `deactivate`
   - Recreate environment: Delete .venv and run `uv venv`

4. **Development Workflow**
   - Add new dependencies: `uv add <package>`
   - Run `uv compile` to update requirements
   - Use `uv sync` to ensure environment matches requirements
   - Commit both `pyproject.toml` and `requirements.txt`

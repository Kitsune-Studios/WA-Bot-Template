# Pre-commit Hooks for WA-Bot-Template

## Overview
This document lists all recommended pre-commit hooks for this project, aligned with the project's tooling and quality standards.

## Core Hooks (Required)

### Python Code Quality
1. `ruff` - Python linter using existing configuration
   - Handles code style, complexity, and best practices
   - Configured via pyproject.toml
   - Enforces typing, docstrings, and code organization

2. `ruff-format`
   - Code formatting following project standards
   - Ensures consistent code style

### UV Package Management
1. `uv-lock`
   - Updates uv.lock file with exact package versions
   - Ensures reproducible environments

2. `uv-export`
   - Exports dependencies to requirements.txt
   - Maintains synchronization between pyproject.toml and requirements.txt

3. `uv-sync`
   - Synchronizes virtual environment with requirements
   - Ensures development environment matches specifications

## Additional Recommended Hooks

### General
1. `trailing-whitespace`
   - Removes trailing whitespace
   - Maintains clean code files

2. `end-of-file-fixer`
   - Ensures files end with a newline
   - Follows Unix file conventions

3. `check-yaml`
   - Validates YAML syntax
   - Important for CI/CD and Pulumi configurations

4. `check-toml`
   - Validates TOML syntax
   - Critical for pyproject.toml maintenance

### Python Specific
1. `debug-statements`
   - Catches debugging statements
   - Prevents accidental commits of debug code

2. `check-docstring-first`
   - Ensures docstrings are at the start of modules
   - Maintains documentation standards

3. `name-tests-test`
   - Enforces test naming conventions
   - Maintains consistent test organization

### Security
1. `detect-private-key`
   - Prevents committing private keys
   - Essential for security

2. `check-added-large-files`
   - Prevents large file commits
   - Maintains repository size

### Docker
1. `check-dockerfile`
   - Validates Dockerfile syntax
   - Important for container builds

## Installation

1. Install pre-commit:
```bash
uv add pre-commit
```

2. Set up the git hooks:
```bash
pre-commit install
```

3. Install specific hooks by adding them to `.pre-commit-config.yaml`

## Current Configuration

The project currently uses these hooks as defined in `.pre-commit-config.yaml`:
```yaml
repos:
  - repo: https://github.com/astral-sh/uv-pre-commit
    rev: 0.5.18
    hooks:
      - id: uv-lock
      - id: uv-export
      - id: uv-sync
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.9.2
    hooks:
      - id: ruff
        args: [ --fix ]
      - id: ruff-format
```

## Running Hooks

- Automatically on commit: Hooks run on staged files
- Manually on all files: `pre-commit run --all-files`
- Single hook: `pre-commit run <hook-id>`

## Best Practices

1. **Never Skip Hooks**
   - Hooks ensure code quality
   - Fix issues rather than bypassing checks

2. **Keep Hooks Updated**
   - Regularly update hook versions
   - Check for new useful hooks

3. **Configure Thoughtfully**
   - Adjust hook settings in `.pre-commit-config.yaml`
   - Balance strictness with productivity

4. **Document Changes**
   - Update this document when modifying hooks
   - Explain hook configuration changes

## Maintenance

1. Update hooks regularly:
```bash
pre-commit autoupdate
```

2. Verify hook functionality:
```bash
pre-commit run --all-files
```

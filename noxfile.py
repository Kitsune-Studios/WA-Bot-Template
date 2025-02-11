"""Nox automation script for project tasks and testing."""

import subprocess
from os import getenv
from pathlib import Path

import nox
from dotenv import load_dotenv
from nox.sessions import Session

# Load environment variables
load_dotenv()

# Constants
PYTHON_VERSION = Path(".python-version").read_text().strip()
PROJECT_NAME = Path.cwd().name
EXTERNAL = getenv("EXTERNAL", "True").lower() == "true"
KEEP_VENV = getenv("KEEP_VENV", "True").lower() == "true"
PORT_NUMBER = int(getenv("PORT_NUMBER", "8000"))
BACKEND = "uv"  # Alternative options: "venv", "conda"

# Default sessions
nox.options.sessions = ["tests"]


def get_docker_name(name: str | None = None) -> str:
    """Return the docker container/image name.

    Args:
        name: Optional custom name. Uses PROJECT_NAME if not provided.

    Returns:
        str: Docker container/image name

    """
    return name if name else PROJECT_NAME


@nox.session(python=["3.11"])
def tests(session: Session) -> None:
    """Run the test suite using the project's settings.

    Instead of installing packages, we first sync the uv configuration
    to make available project settings from pyproject.toml.
    """
    session.run("uv", "sync", "--all-groups", external=EXTERNAL)
    session.run("pytest", *session.posargs)


# Docker management commands
@nox.session(python=PYTHON_VERSION, venv_backend=BACKEND, reuse_venv=KEEP_VENV)
def docker(session: Session) -> None:
    """Build and run the project in a Docker container."""
    docker_name = get_docker_name()
    session.log(f"Building Docker image: {docker_name}")
    session.run("docker", "build", "-t", docker_name, ".", external=EXTERNAL)
    docker_run(session, docker_name)


@nox.session(python=PYTHON_VERSION, venv_backend=BACKEND, reuse_venv=KEEP_VENV)
def docker_run(session: Session, docker_name: str) -> None:
    """Run a Docker container with the specified configuration.

    Args:
        session: Nox session instance for running commands
        docker_name: Name of the Docker image to run

    """
    session.run(
        "docker",
        "run",
        "--name",
        docker_name,
        "-p",
        f"{PORT_NUMBER}:{PORT_NUMBER}",
        "-d",
        docker_name,
        external=EXTERNAL,
    )


@nox.session(python=PYTHON_VERSION, venv_backend=BACKEND, reuse_venv=KEEP_VENV)
def docker_stop(session: Session, docker_name: str | None = None) -> None:
    """Stop a running Docker container."""
    name = get_docker_name(docker_name)
    session.log(f"Stopping Docker container: {name}")
    session.run("docker", "stop", name, external=EXTERNAL)


@nox.session(python=PYTHON_VERSION, venv_backend=BACKEND, reuse_venv=KEEP_VENV)
def docker_start(session: Session, docker_name: str | None = None) -> None:
    """Start a stopped Docker container."""
    name = get_docker_name(docker_name)
    session.log(f"Starting Docker container: {name}")
    session.run("docker", "start", name, external=EXTERNAL)


@nox.session(python=PYTHON_VERSION, venv_backend=BACKEND, reuse_venv=KEEP_VENV)
def docker_rm(session: Session, docker_name: str | None = None) -> None:
    """Remove a Docker container."""
    name = get_docker_name(docker_name)
    docker_stop(session, name)
    session.log(f"Removing Docker container: {name}")
    session.run("docker", "rm", name, external=EXTERNAL)


@nox.session(python=PYTHON_VERSION, venv_backend=BACKEND, reuse_venv=KEEP_VENV)
def docker_rmi(session: Session, docker_name: str | None = None) -> None:
    """Remove a Docker image and its container."""
    name = get_docker_name(docker_name)
    docker_rm(session, name)
    session.log(f"Removing Docker image: {name}")
    session.run("docker", "rmi", name, external=EXTERNAL)


# Development commands
@nox.session(python=PYTHON_VERSION, venv_backend=BACKEND, reuse_venv=KEEP_VENV)
def dev(session: Session) -> None:
    """Run the project in development mode."""
    try:
        session.run("uv", "sync", "--all-groups", external=EXTERNAL)
        session.run("uv", "run", "./main.py", external=EXTERNAL)
    except (subprocess.CalledProcessError, OSError) as e:
        session.error(f"Development server failed: {e}")


@nox.session(python=PYTHON_VERSION, venv_backend=BACKEND, reuse_venv=KEEP_VENV)
def setup_pre_commit(session: Session) -> None:
    """Configure pre-commit and pre-push hooks."""
    try:
        session.run("pre-commit", "install", external=EXTERNAL)
        session.run("pre-commit", "install", "-t", "pre-push", external=EXTERNAL)
    except (subprocess.CalledProcessError, OSError) as e:
        session.error(f"Failed to setup pre-commit hooks: {e}")

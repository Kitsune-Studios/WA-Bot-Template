import pathlib

import nox
from nox.sessions import Session

PYTHON_VERSION = pathlib.Path(".python-version").read_text().strip()
python_version = PYTHON_VERSION  # choose the python version you want to use
python_matrix = ["3.11", "3.12", "3.13"]
python_matrix = python_version if python_version != "" else python_matrix
backend = "uv"  # or "venv" or "conda"
name = "kitsune-backend"
# nox options

# default sessions when run nox. By default, nox will run all sessions on the list
nox.options.sessions = [
    "lint",
    "format",
    "tests",
    "docker",
]


# nox automation to run the project using uv


@nox.session(python=python_matrix, venv_backend=backend)
def lint(session: Session) -> None:
    """Run ruff linter."""
    session.run("uvx", "ruff", "check", ".")


@nox.session(python=python_matrix, venv_backend=backend)
def format(session: Session) -> None:
    """Run ruff formatter."""
    session.run("uvx", "ruff", "format", "--target-version=py312", ".")


@nox.session(python=python_matrix, venv_backend=backend, reuse_venv=True)
def tests(session: Session) -> None:
    """Run the pytest test suite."""
    session.run("pytest", "--cov", env={"COVERAGE_FILE": ".coverage"})


# non-default sessions to run


@nox.session(python=python_matrix, venv_backend=backend, reuse_venv=True)
def docker_run(session: nox.Session, docker_name: str) -> None:
    """Run the project dev environment in docker container."""
    session.run(
        "docker",
        "run",
        "--name",
        name,
        "-p",
        "8000:8000",
        "-d",
        docker_name,
    )


@nox.session(python=python_version, venv_backend=backend, reuse_venv=True)
def docker(session: nox.Session) -> None:
    """Build & Run the project dev environment in docker container."""

    session.run("docker", "build", "-t", name, ".")
    docker_run(session, name)


@nox.session(python=python_matrix, venv_backend=backend, reuse_venv=True)
def docker_stop(session: nox.Session, docker_name: str = "") -> None:
    """Stop the running docker container."""
    docker_name = name if docker_name == "" else docker_name
    session.run("docker", "stop", docker_name)

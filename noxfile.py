# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "python-dotenv",
#     "nox",
# ]
# ///
"""Main nox automation script."""

import pathlib
from os import getenv

import nox
import nox.command
from dotenv import load_dotenv
from nox.sessions import Session

load_dotenv()

PORT_NUMBER = int(getenv("PORT_NUMBER", "8000"))
PYTHON_VERSION = (
    pathlib.Path(".python-version").read_text().strip()
)  # read python version from .python-version file
python_version = PYTHON_VERSION

python_matrix = ["3.11", "3.12", "3.13"] if python_version == "" else python_version

python_matrix = python_version if python_version != "" else python_matrix

backend = "uv"  # or "venv" or "conda"

name = (
    pathlib.Path("./pyproject.toml")
    .read_text()
    .split("\n")[1]
    .split("=")[1]
    .strip()
    .replace('"', "")
)
# nox options

# default sessions when run nox without specifying any session
nox.options.sessions = [
    "lint",  #  to run linter
    "fmt",  #  to run formatter
    # "run_tests",  # to run tests
]


# nox automation to run the project using uv


@nox.session(python=python_matrix, venv_backend=backend)
def lint(session: Session) -> None:
    """Run ruff linter."""
    session.run("uvx", "ruff", "check", "--fix", "--unsafe-fixes", ".")


@nox.session(python=python_matrix, venv_backend=backend)
def fmt(session: Session) -> None:
    """Run ruff formatter."""
    session.run("uvx", "ruff", "format", "--target-version=py312")


@nox.session(python=python_matrix, venv_backend=backend, reuse_venv=True)
def run_tests(session: Session) -> None:
    """Run the pytest test suite."""
    try:
        session.run(
            "pytest",
            "--cov",
            env={"COVERAGE_FILE": ".coverage"},
            external=True,
        )
    except nox.command.CommandFailed(Exception) as e:
        session.warn(e)


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
        str(PORT_NUMBER) + ":" + str(PORT_NUMBER),
        "-d",
        docker_name,
    )


@nox.session(python=python_version, venv_backend=backend, reuse_venv=True)
def docker(session: nox.Session) -> None:
    """Build & Run the project dev environment in docker container."""
    session.log("Building the docker image: %s", name)
    session.run("docker", "build", "-t", name, ".")
    docker_run(session, name)


@nox.session(python=python_matrix, venv_backend=backend, reuse_venv=True)
def docker_stop(session: nox.Session, docker_name: str = "") -> None:
    """Stop the running docker container."""
    session.log("Stopping the docker container: %s", docker_name)
    docker_name = name if docker_name == "" else docker_name
    session.run("docker", "stop", docker_name)


@nox.session(python=python_matrix, venv_backend=backend, reuse_venv=True)
def docker_start(session: nox.Session, docker_name: str = "") -> None:
    """Start the stopped docker container."""
    docker_name = name if docker_name == "" else docker_name
    session.log("Starting the docker container: %s", docker_name)
    session.run("docker", "start", docker_name)


@nox.session(python=python_matrix, venv_backend=backend, reuse_venv=True)
def docker_rm(session: nox.Session, docker_name: str = "") -> None:
    """Remove the docker container."""
    docker_name = name if docker_name == "" else docker_name
    session.log("Stopping the docker container if any: %s", docker_name)
    docker_stop(session, docker_name)
    session.log("Removing the docker container: %s", docker_name)
    session.run("docker", "rm", docker_name)


@nox.session(python=python_matrix, venv_backend=backend, reuse_venv=True)
def docker_rmi(session: nox.Session, docker_name: str = "") -> None:
    """Remove the docker image."""
    session.log("Removing the docker container if any: %s", docker_name)
    docker_rm(session, docker_name)
    session.log("Removing the docker image: %s", docker_name)
    docker_name = name if docker_name == "" else docker_name
    session.run("docker", "rmi", docker_name)


@nox.session(python=python_matrix, venv_backend=backend, reuse_venv=True)
def dev(session: nox.Session) -> None:
    """Run the project dev environment locally."""
    session.run("uv", "run", "./main.py")

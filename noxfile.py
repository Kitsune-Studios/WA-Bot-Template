import pathlib

import nox
from nox.sessions import Session

PYTHON_VERSION = pathlib.Path(".python-version").read_text().strip()
python_version = PYTHON_VERSION  # choose the python version you want to use
python_matrix = ["3.11", "3.12", "3.13"]
python_matrix = python_version if python_version != "" else python_matrix
backend = "uv"  # or "venv" or "conda"

# nox options

# default sessions when run nox. By default, nox will run all sessions on the list
nox.options.sessions = [
    "dev",
    "lint",
    "format",
    "test",
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
def test(session: Session) -> None:
    """Run the pytest test suite."""
    session.run("uv", "")
    session.run("pytest", "--cov", env={"COVERAGE_FILE": ".coverage"})


# non-default sessions to run
@nox.session(python=python_version, venv_backend=backend, reuse_venv=True)
def dev(session: nox.Session) -> None:
    """Run the project dev envirioment."""
    name = session.posargs[0] if session.posargs else "Lautaro"
    # check if docker client is installed
    session.log(f">Hello {name}: docker is not installed")
    session.log(f">Python version: {PYTHON_VERSION}")

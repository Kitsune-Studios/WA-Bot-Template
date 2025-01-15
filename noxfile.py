import nox
from nox.sessions import Session

python_version = "3.12"  # choose the python version you want to use
python_matrix = ["3.10", "3.11", "3.12", "3.13"]
python_matrix = python_version if python_version != "" else python_matrix
backend = "uv"  # or "venv" or "conda"

# nox options

# default sessions to run
nox.options.sessions = ["format", "lint", "test"]  # default sessions to run


# nox automation to run the project using uv


@nox.session(python=python_matrix, venv_backend=backend)
def test(session: Session) -> None:
    """Run the test suite."""
    session.run("uv", "add", "--dev", "pytest", "pytest-cov", ".")
    session.run("pytest", "--cov", env={"COVERAGE_FILE": ".coverage"})


@nox.session(python=python_matrix, venv_backend=backend)
def format(session: Session) -> None:
    """Run black and isort."""
    session.run("uv", "add", "--dev", "black", "isort")
    session.run("isort", ".")
    session.run("black", ".")


@nox.session(python=python_matrix, venv_backend=backend)
def lint(session: Session) -> None:
    """Run flake8."""
    session.run(
        "uv",
        "add",
        "--dev",
        "flake8",
        "flake8-bugbear",
        "flake8-import-order",
        "flake8-pyproject",
        "flake8-bandit",
        "darglint",
    )
    session.run("flake8", ".")


# nox automation to run the project using docker
@nox.session(python=python_version, venv_backend=backend)
def local_docker(session: Session) -> None:
    """Run the project using docker."""
    session.run("docker-compose", "up", "--build")

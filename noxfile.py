import nox
from nox.sessions import Session

python_version = "3.12"  # choose the python version you want to use
python_matrix = ["3.10", "3.11", "3.12", "3.13"]
python_matrix = python_version if python_version != "" else python_matrix
backend = "uv"  # or "venv" or "conda"

# nox options

# default sessions to run
nox.options.sessions = [
    "lint",
    "format",
    # "test",
]  # default sessions if run locally, order matters


# nox automation to run the project using uv


@nox.session(python=python_matrix, venv_backend=backend)
def lint(session: Session) -> None:
    """Run ruff linter."""
    session.run("uv", "add", "--dev", "ruff")
    session.run("ruff", "check", ".")


@nox.session(python=python_matrix, venv_backend=backend)
def format(session: Session) -> None:
    """Run ruff formatter."""
    session.run("uv", "add", "--dev", "ruff")
    session.run("ruff", "format", "--target-version=py312", ".")


@nox.session(python=python_matrix, venv_backend=backend)
def test(session: Session) -> None:
    """Run the test suite."""
    session.run("uv", "add", "--dev", "pytest", "pytest-cov", ".")
    session.run("pytest", "--cov", env={"COVERAGE_FILE": ".coverage"})


# non-default sessions to run
@nox.session(python=python_version, venv_backend=backend)
def dev(session: Session) -> None:
    """Run the project using docker."""
    session.run("docker-compose", "up", "--build")

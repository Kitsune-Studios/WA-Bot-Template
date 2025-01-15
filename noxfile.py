import nox
from nox.sessions import Session

nox.options.sessions = ["format", "lint", "test", "docs", "build", "publish"]

python_versions = ["3.8", "3.9", "3.10", "3.11", "3.12"]


@nox.session(python=python_versions)
def test(session: Session) -> None:
    """Run the test suite."""
    session.run("uv", "install", "pytest", "pytest-cov", ".")
    session.run("pytest", "--cov", env={"COVERAGE_FILE": ".coverage"})


@nox.session(python=python_versions)
def format(session: Session) -> None:
    """Run black and isort."""
    session.run("uv", "install", "black", "isort")
    session.run("isort", ".")
    session.run("black", ".")


@nox.session(python=python_versions)
def lint(session: Session) -> None:
    """Run flake8."""
    session.run(
        "uv",
        "install",
        "flake8",
        "flake8-bugbear",
        "flake8-import-order",
        "flake8-pyproject",
        "flake8-bandit",
        "darglint",
    )
    session.run("flake8", ".")

"""Main test file."""

from fastapi import FastAPI
from fastapi.testclient import TestClient

from backend.services.messaging import STATUS_OK

app = FastAPI()


@app.get("/")
async def read_main() -> dict[str, str]:
    """Read main function."""
    return {"msg": "Hello World"}


client = TestClient(app)


def test_read_main() -> None:
    """Test read_main function."""
    response = client.get("/")
    assert response.status_code == STATUS_OK
    assert response.json() == {"msg": "Hello World"}

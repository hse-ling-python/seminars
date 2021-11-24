import pytest

from app import app


@pytest.fixture
def client():
    client = app.test_client()
    yield client


def test_root(client):
    r = client.get("/")
    assert b"Hello world" == r.data


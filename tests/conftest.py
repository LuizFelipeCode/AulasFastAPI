import pytest
from fastapi.testclient import TestClient

from estudo_fast.app import app


@pytest.fixture
def client():
    return TestClient(app)

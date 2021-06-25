import pytest
from main import app


@pytest.fixture
def client():
    """App fixture"""
    with app.test_client() as client:
        yield client

import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_hello(client):
    res = client.get("/")
    assert res.status_code == 200
    assert res.get_json() == {"message": "Hello, world"}
    
    
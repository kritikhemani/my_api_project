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
  
def test_echo(client):
    res = client.post("/echo", json={"name": " "})
    assert res.status_code == 201
    assert res.get_json() == {"you_sent": {"name": " "}}
  
    
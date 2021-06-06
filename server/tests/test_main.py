from fastapi.testclient import TestClient

from app.main import app, BasicRequest, Options

client = TestClient(app)


def test_read_main():
    data = {"data": '{"foo": 5}'}
    response = client.post("/", json=data)
    assert response.status_code == 200

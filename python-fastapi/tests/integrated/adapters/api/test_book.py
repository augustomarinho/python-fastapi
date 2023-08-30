from starlette.testclient import TestClient

from app.main import app, create_routes

client = TestClient(app)
create_routes()


def test_read_books():
    response = client.get("/api/v1/books")
    assert response.status_code == 200

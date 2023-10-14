import datetime
from unittest.mock import AsyncMock

import pytest
from starlette.testclient import TestClient

from app.configs.depency_injection import Container
from app.domain.models.book import Book
from app.domain.ports.book import BookPort
from app.main import app, create_routes


@pytest.fixture
def book() -> Book:
    return Book(name="Test Book",
                author="Augusto Marinho",
                created_at=datetime.datetime.now(tz=datetime.timezone.utc),
                isbn="1234567890")


@pytest.fixture
async def mock_book_port(book):
    return AsyncMock(spec=BookPort,
                     create_book=AsyncMock(return_value=book),
                     get_book_by_id=AsyncMock(return_value=book)
                     )


@pytest.fixture
def container(mocker, mock_book_port):
    container = Container()
    container.db_engine.override(mocker.Mock())
    container.book_port.override(mock_book_port)
    return container


@pytest.fixture
def client(container):
    create_routes()
    app.container = container
    return TestClient(app)


def test_read_books(client):
    # Given
    response = client.get("/api/v1/books")

    # Then
    assert response.status_code == 200


def test_create_book(client):
    # Given
    response = client.post("/api/v1/books",
                           follow_redirects=False,
                           json={
                               "book_name": "Test Book",
                               "book_author": "Augusto Marinho",
                               "book_isbn": "1234567890"
                           }
                           )

    # Then
    assert response.status_code == 201


def test_read_book_by_id(client, book):
    # When
    book.id = 1

    # Given
    response = client.get("/api/v1/books/1",
                          follow_redirects=False
                          )

    # Then
    json = response.json()
    assert response.status_code == 200
    assert json["book_isbn"] == book.isbn

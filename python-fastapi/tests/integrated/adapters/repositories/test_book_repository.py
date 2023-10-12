import datetime

import pytest

from app.adapters.repositories.book import BookRepository
from app.domain.models.book import Book


@pytest.mark.asyncio
async def test_create_book(async_engine):
    # When
    book_port = BookRepository(async_engine)

    # Given
    book = Book(name="Test Book",
                author="Augusto Marinho",
                created_at=datetime.datetime.now(),
                isbn="1234567890")

    persited_book = await book_port.create_book(book)

    # Then
    assert persited_book is not None
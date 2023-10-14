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
                created_at=datetime.datetime.now(tz=datetime.timezone.utc),
                isbn="1234567890")

    persited_book = await book_port.create_book(book)

    # Then
    assert persited_book.id is not None
    assert persited_book.name == book.name
    assert persited_book.author == book.author
    assert persited_book.isbn == book.isbn
    assert persited_book.created_at == book.created_at


@pytest.mark.asyncio
async def test_update_book(async_engine):

    # When
    book_port = BookRepository(async_engine)

    # Given
    book = Book(name="Test Book",
                author="Augusto Marinho",
                created_at=datetime.datetime.now(tz=datetime.timezone.utc),
                isbn="1234567890")

    persited_book = await book_port.create_book(book)
    persited_book.author = "Augusto Marinho 2"

    updated_book = await book_port.update_book(persited_book)

    # Then
    assert updated_book.id is not None
    assert updated_book.name == persited_book.name
    assert updated_book.author == persited_book.author
    assert updated_book.isbn == persited_book.isbn
    assert updated_book.created_at == persited_book.created_at
    assert updated_book.updated_at is not None


@pytest.mark.asyncio
async def test_get_book_by_id(async_engine):
    # When
    book_port = BookRepository(async_engine)

    # Given
    book = Book(name="Test Book",
                author="Augusto Marinho",
                created_at=datetime.datetime.now(tz=datetime.timezone.utc),
                isbn="1234567890")

    persited_book = await book_port.create_book(book)
    readed_book = await book_port.get_book_by_id(persited_book.id)

    # Then
    assert readed_book.id is not None
    assert readed_book.name == persited_book.name
    assert readed_book.author == persited_book.author
    assert readed_book.isbn == persited_book.isbn
    assert readed_book.created_at == persited_book.created_at
    assert readed_book.updated_at is None


@pytest.mark.asyncio
async def test_get_delete_book_by_id(async_engine):
    # When
    book_port = BookRepository(async_engine)

    # Given
    book = Book(name="Test Book",
                author="Augusto Marinho",
                created_at=datetime.datetime.now(tz=datetime.timezone.utc),
                isbn="1234567890")

    persited_book = await book_port.create_book(book)
    await book_port.delete_book(persited_book.id)
    readed_book = await book_port.get_book_by_id(persited_book.id)

    # Then
    assert readed_book is None

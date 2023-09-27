from datetime import datetime

from sqlalchemy import Engine, text

from app.domain.models.book import Book
from app.domain.ports.book_ports import BookPort


class BookRepository(BookPort):

    def __init__(self, db_engine: Engine):
        self.db_engine = db_engine

    async def get_book_by_id(self, book_id: int) -> Book | None:
        async with self.db_engine.connect() as conn:
            stmt = text(
                """SELECT id, name, author, isbn, created_at, updated_at
                FROM books
                WHERE id = :id
                """
            )
            stmt = stmt.bindparams(id=book_id)
            result = await conn.execute(stmt)
            raw_book = result.fetchone()

            if raw_book:
                return Book.model_validate(raw_book._mapping)
            return None

    async def create_book(self, book: Book) -> Book:
        async with self.db_engine.connect() as conn:
            stmt = text(
                """INSERT INTO books (name, author, isbn, created_at)
                VALUES (:name, :author, :isbn, :created_at)
                RETURNING id, name, author, isbn, created_at, updated_at
                """
            )
            stmt = stmt.bindparams(name=book.name,
                                   author=book.author,
                                   isbn=book.isbn,
                                   created_at=book.created_at)
            result = await conn.execute(stmt)
            raw_book = result.fetchone()

            return Book.model_validate(raw_book._mapping)

    async def update_book(self, book: Book) -> Book | None:
        async with self.db_engine.connect() as conn:
            stmt = text(
                """
                UPDATE books
                SET name = :name, author = :author, isbn = :isbn, updated_at = :updated_at
                WHERE id = :id
                RETURNING id, name, author, isbn, created_at, updated_at    
                """
            )
            stmt = stmt.bindparams(id=book.id,
                                   name=book.name,
                                   author=book.author,
                                   isbn=book.isbn,
                                   updated_at=datetime.now())
            result = await conn.execute(stmt)
            raw_book = result.fetchone()

            if raw_book:
                return Book.model_validate(raw_book._mapping)

            return None

    async def delete_book(self, book_id: int):
        async with self.db_engine.connect() as conn:
            stmt = text(
                """DELETE FROM books WHERE id = :id"""
            )
            stmt = stmt.bindparams(id=book_id)
            await conn.execute(stmt)

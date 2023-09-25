from abc import ABC, abstractmethod

from app.domain.models.book_model import Book


class BookPort(ABC):

    @abstractmethod
    async def get_book_by_id(self, book_id: int) -> Book | None:
        pass

    @abstractmethod
    async def create_book(self, book: Book) -> Book:
        pass

    @abstractmethod
    async def update_book(self, book: Book) -> Book | None:
        pass

    @abstractmethod
    async def delete_book(self, book_id: int):
        pass

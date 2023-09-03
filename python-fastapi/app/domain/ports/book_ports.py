from abc import ABC, abstractmethod


class BookPort(ABC):

    @abstractmethod
    def get_book_by_id(self, book_id: int):
        pass

    @abstractmethod
    def create_book(self, book):
        pass

    @abstractmethod
    def update_book(self, book):
        pass

    @abstractmethod
    def delete_book(self, book_id: int):
        pass
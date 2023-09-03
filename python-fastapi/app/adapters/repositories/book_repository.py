from sqlalchemy import Engine

from app.domain.ports.book_ports import BookPort


class BookRepository(BookPort):

    def __init__(self, db_engine: Engine):
        self.db_engine = db_engine

    def get_book_by_id(self, book_id: int):
        pass

    def create_book(self, book):
        pass

    def update_book(self, book):
        pass

    def delete_book(self, book_id: int):
        pass
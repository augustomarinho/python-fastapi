from pydantic import BaseModel


class CreateBookV1Request(BaseModel):
    book_name: str
    book_author: str
    book_isbn: str


class CreateBookV1Response(BaseModel):
    book_isbn: str


class CreateBookV1ListResponse(BaseModel):
    books: list[CreateBookV1Response]

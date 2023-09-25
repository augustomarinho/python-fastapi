from datetime import datetime

from dependency_injector.wiring import Provide, inject
from fastapi import Response, status, APIRouter, Depends

from app.adapters.entrypoints.http import http
from app.adapters.entrypoints.http.v1 import book_dto
from app.domain.models.book_model import Book
from app.domain.ports.book_ports import BookPort
from app.configs.depency_injection import Container

router1 = APIRouter()


@router1.get("/api/v1/books",
             response_model=book_dto.CreateBookV1ListResponse
             )
async def read_all_book(
        response: Response
) -> book_dto.CreateBookV1ListResponse:
    list_book = [
        book_dto.CreateBookV1Response(book_isbn="123"),
        book_dto.CreateBookV1Response(book_isbn="456"),
    ]
    response.status_code = status.HTTP_200_OK
    return book_dto.CreateBookV1ListResponse(books=list_book)


@router1.get("/api/v1/books/{book_id}",
             response_model=book_dto.CreateBookV1Response
             )
@inject
async def read_book(
        book_id: int,
        response: Response,
        book_port: BookPort = Depends(Provide[Container.book_port])
) -> book_dto.CreateBookV1Response:
    response.status_code = status.HTTP_200_OK
    book = await book_port.get_book_by_id(book_id=book_id)

    if book:
        return book_dto.CreateBookV1Response(book_isbn=book.isbn)
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return book_dto.CreateBookV1Response()


@router1.post("/api/v1/books",
              response_model=book_dto.CreateBookV1Response
              )
@inject
async def create_book(
        create_book_request: book_dto.CreateBookV1Request,
        response: Response,
        book_port: BookPort = Depends(Provide[Container.book_port]),
) -> book_dto.CreateBookV1Response:
    book = Book(name=create_book_request.book_name,
                author=create_book_request.book_author,
                isbn=create_book_request.book_isbn,
                created_at=datetime.now())
    book = await book_port.create_book(book)

    response.status_code = status.HTTP_201_CREATED
    response.headers[
        http.HEADER_CONTENT_TYPE
    ] = http.HEADER_CONTENT_TYPE_APPLICATION_JSON
    return book_dto.CreateBookV1Response(
        book_isbn=book.isbn,
    )
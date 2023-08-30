from fastapi import status, Response
from pydantic import BaseModel

import app.infrastructure.http as http
from app.infrastructure.fastapi_router import FastAPIRouterController


class CreateBookRequest(BaseModel):
    book_name: str
    book_author: str
    book_isbn: str


class CreateBookResponse(BaseModel):
    book_isbn: str


class CreateBookListResponse(BaseModel):
    books: list[CreateBookResponse]


class BookV1API:

    def __init__(self, app_route_controller: FastAPIRouterController):
        app_route_controller = app_route_controller
        app_route_controller.add_api_route(
            "/api/v1/books",
            self.read_all_book,
            methods=["GET"],
            response_model=CreateBookListResponse,
        )
        app_route_controller.add_api_route(
            "/api/v1/books/{book_id}",
            self.read_book,
            methods=["GET"],
            response_model=CreateBookResponse,
        )

        app_route_controller.include_router()


    async def read_all_book(self, response: Response) -> CreateBookListResponse:
        list_book = [
            CreateBookResponse(book_isbn="123"),
            CreateBookResponse(book_isbn="456"),
        ]
        response.status_code = status.HTTP_200_OK
        return CreateBookListResponse(books=list_book)


    def read_book(self, book_id: int, response: Response) -> CreateBookResponse:
        response.status_code = status.HTTP_200_OK
        return CreateBookResponse(book_isbn=book_id)


    def create_book(
            self, create_book_request: CreateBookRequest, response: Response
    ) -> CreateBookResponse:
        response.status_code = status.HTTP_201_CREATED
        response.headers[
            http.HEADER_CONTENT_TYPE
        ] = http.HEADER_CONTENT_TYPE_APPLICATION_JSON
        return CreateBookResponse(book_isbn=create_book_request.book_isbn)

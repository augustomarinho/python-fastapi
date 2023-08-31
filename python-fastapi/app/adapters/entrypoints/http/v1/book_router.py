from fastapi import Response, status

import app.adapters.entrypoints.http.http as http
from app.adapters.entrypoints.http.fastapi_router import (
    FastAPIRouterController
)
from app.adapters.entrypoints.http.v1 import book_dto


class BookV1API:
    def __init__(self, app_route_controller: FastAPIRouterController):
        app_route_controller = app_route_controller
        app_route_controller.add_api_route(
            "/api/v1/books",
            self.read_all_book,
            methods=["GET"],
            response_model=book_dto.CreateBookV1ListResponse,
        )
        app_route_controller.add_api_route(
            "/api/v1/books/{book_id}",
            self.read_book,
            methods=["GET"],
            response_model=book_dto.CreateBookV1Response,
        )

        app_route_controller.include_router()

    async def read_all_book(
        self, response: Response
    ) -> book_dto.CreateBookV1ListResponse:
        list_book = [
            book_dto.CreateBookV1Response(book_isbn="123"),
            book_dto.CreateBookV1Response(book_isbn="456"),
        ]
        response.status_code = status.HTTP_200_OK
        return book_dto.CreateBookV1ListResponse(books=list_book)

    def read_book(
        self, book_id: int, response: Response
    ) -> book_dto.CreateBookV1Response:
        response.status_code = status.HTTP_200_OK
        return book_dto.CreateBookV1Response(book_isbn=book_id)

    def create_book(
        self,
        create_book_request: book_dto.CreateBookV1Request,
        response: Response,
    ) -> book_dto.CreateBookV1Response:
        response.status_code = status.HTTP_201_CREATED
        response.headers[
            http.HEADER_CONTENT_TYPE
        ] = http.HEADER_CONTENT_TYPE_APPLICATION_JSON
        return book_dto.CreateBookV1Response(
            book_isbn=create_book_request.book_isbn
        )

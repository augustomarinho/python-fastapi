from fastapi import Response, status, APIRouter

from app.adapters.entrypoints.http.v1 import book_dto

router1 = APIRouter(prefix="/v1")


@router1.get("/api/v1/books",
            response_model=book_dto.CreateBookV1ListResponse
            )
async def read_all_book(
        self, response: Response
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
def read_book(
        self, book_id: int, response: Response
) -> book_dto.CreateBookV1Response:
    response.status_code = status.HTTP_200_OK
    return book_dto.CreateBookV1Response(book_isbn=str(book_id))


# def create_book(
#         self,
#         create_book_request: book_dto.CreateBookV1Request,
#         response: Response,
# ) -> book_dto.CreateBookV1Response:
#     response.status_code = status.HTTP_201_CREATED
#     response.headers[
#         http.HEADER_CONTENT_TYPE
#     ] = http.HEADER_CONTENT_TYPE_APPLICATION_JSON
#     return book_dto.CreateBookV1Response(
#         book_isbn=create_book_request.book_isbn
#     )
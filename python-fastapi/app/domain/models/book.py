from typing import Optional

from app.domain.models.models import BaseDateModel


class Book(BaseDateModel):

    id: Optional[int] = None
    name: str
    author: str
    isbn: str

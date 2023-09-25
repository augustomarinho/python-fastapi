from typing import Optional

from pydantic import Field

from app.domain.models.models import BaseDateModel


class Book(BaseDateModel):

    id: Optional[int] = Field(default=None, description="Internal Book ID.")
    name: str = Field(default=..., description="Book name.")
    author: str = Field(default=..., description="Book author.")
    isbn: str = Field(default=..., description="Book ISBN.")

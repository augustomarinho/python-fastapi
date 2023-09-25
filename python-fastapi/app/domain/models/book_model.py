from pydantic import Field
from sqlalchemy import Column, Integer, String

from app.domain.models.models import BaseDateModel


class Book(BaseDateModel):

    id: int = Field(default=..., description="Internal Book ID.")
    name = Field(default=..., description="Book name.")
    author = Field(default=..., description="Book author.")
    isbn = Field(default=..., description="Book ISBN.")
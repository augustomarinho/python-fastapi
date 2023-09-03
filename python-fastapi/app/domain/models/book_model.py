from sqlalchemy import Column, Integer, String

from app.domain.models.models import BaseDateModel


class Book(BaseDateModel):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, index=True)
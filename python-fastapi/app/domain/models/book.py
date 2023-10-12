from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Book(BaseModel):

    id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    name: str
    author: str
    isbn: str

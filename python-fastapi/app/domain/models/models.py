from typing import Optional

from pydantic import Field
from datetime import datetime

from pydantic import BaseModel


class BaseDateModel(BaseModel):

    created_at: Optional[datetime] = Field(None, description="Date of creation.")
    updated_at: Optional[datetime] = Field(None, description="Date of last update.")

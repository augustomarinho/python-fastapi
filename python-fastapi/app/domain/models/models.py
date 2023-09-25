from dataclasses import Field
from datetime import datetime

from pydantic import BaseModel


class BaseDateModel(BaseModel):

    created_at: datetime = Field(..., description="Date of creation.")
    updated_at: datetime = Field(..., description="Date of last update.")

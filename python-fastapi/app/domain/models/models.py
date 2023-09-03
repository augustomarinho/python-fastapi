from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

Base = declarative_base()

class BaseDateModel(Base):
    __abstract__ = True  # Set this to True to make it an abstract base model

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<{self.__class__.__name__}(id={self.id})>"
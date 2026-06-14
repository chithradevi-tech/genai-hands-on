from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy import DateTime
from sqlalchemy.sql import func

from .database import Base

class Note(Base):

    __tablename__ = "notes"

    id = Column(Integer, primary_key=True)

    note_text = Column(Text)

    created_at = Column(
        DateTime,
        server_default=func.now()
    )
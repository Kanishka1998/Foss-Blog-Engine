from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
)

from .meta import Base


class Comment(Base):
    __tablename__ = 'Comment'
    id = Column(Integer, primary_key=True)
    email = Column(Text)
    topic = Column(Text)
    comment = Column(Text)
    datetime = Column(Text)


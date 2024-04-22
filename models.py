from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class DBAuthor(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, unique=True)
    bio = Column(String(1024))
    books = relationship("Book", back_populates="author")


class DBBook(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255))
    summary = Column(String(255))
    publication_date = Column(Date())
    author_id = Column(Integer, ForeignKey('author.id'))

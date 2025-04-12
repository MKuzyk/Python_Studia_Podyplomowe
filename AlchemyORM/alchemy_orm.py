import datetime
from typing import Optional,Annotated,List
from sqlalchemy import *
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, sessionmaker, relationship

str255 = Annotated[str,mapped_column(String(255))]
intpk = Annotated[int, mapped_column(Integer,primary_key=True, autoincrement=True)]

library_metadata = MetaData(schema = 'library_orm')

class Base (DeclarativeBase):
    metadata = library_metadata

class Author(Base):
    __tablename__ ='author'

    id: Mapped[intpk]
    name :  Mapped[str]
    email : Mapped[str255]
    login : Mapped[str] = mapped_column(String(100), default='No Login')
    middle_name: Mapped[Optional[str]]

    books: Mapped[List['Book']] = relationship (back_populates='author', cascade='delete,delete-orphan')
    address: Mapped['Address'] = relationship(back_populates='author',cascade='delete,delete-orphan')

class Address(Base):
    __tablename__ ='address'

    id: Mapped[intpk]
    country: Mapped[str255]
    city: Mapped[str255]
    author_id: Mapped[int] = mapped_column(ForeignKey('author.id'))

    author: Mapped['Author'] = relationship(back_populates='author')

class Book(Base):
    __tablename__ ='book'

    id: Mapped[intpk]
    title: Mapped[str255]
    description : Mapped[Optional[str]]
    publication_date: Mapped[datetime.date]

    author_id: Mapped[int] = mapped_column(ForeignKey('author.id'))

    author: Mapped['Author'] = relationship(back_populates='books')

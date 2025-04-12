import datetime
from typing import Optional,Annotated,List
from sqlalchemy import *
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, sessionmaker, relationship

str255 = Annotated[str,mapped_column(String(255))]
intpk = Annotated[int, mapped_column(Integer,primary_key=True, autoincrement=True)]

library_metadata = MetaData(schema = 'library_orm')

class Base (DeclarativeBase):
    metadata = library_metadata

class Users(Base):
    __tablename__ ='users'

    id: Mapped[intpk]
    name :  Mapped[str]
    email : Mapped[str255]
    login : Mapped[str] = mapped_column(String(100), default='No Login')
    middle_name: Mapped[Optional[str]]

    books: Mapped[List['Book']] = relationship (back_populates='user', cascade='delete')

class Book(Base):
    __tablename__ ='book'

    id: Mapped[intpk]
    title: Mapped[str255]
    description : Mapped[Optional[str]]
    publication_date: Mapped[datetime.date]

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    user: Mapped['User'] = relationship(back_populates='books')

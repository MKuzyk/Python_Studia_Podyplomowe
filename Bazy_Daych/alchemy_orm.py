from sqlalchemy import *
from sqlalchemy.orm import declarative_base, mapped_column, Mapped

class Base (declarative_base):
    pass

class Users(Base):
    __tablename__ ='users'

    id: Mapped[int] = mapped_column (primary_key=True,autoincrement=True)
    name :  Mapped[str]
    email : Mapped[str] = mapped_column(String(255))
    login : Mapped[str] = mapped_column(String(255), default='No Login')
    middle_name: Mapped[str]
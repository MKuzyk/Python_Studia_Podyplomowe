from sqlalchemy import *
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Users(Base):
    __tablename__ ='users'

    id = Column (Integer,primary_key=True,autoincrement=True)
    name = Column(String) #Varchar(Max)
    email = Column(String(255))
    login = Column(String(100), default='No Login')
    middle_name = Column (String(255),nullable=True)
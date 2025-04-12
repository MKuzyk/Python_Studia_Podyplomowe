from dotenv import load_dotenv
import os
from sqlalchemy.schema import CreateSchema

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from Alchemy_ORM.Laboratorium_4 import User, ShippingAddress, Cart, Product, CartProduct

# Wczytanie zmiennych środowiskowych
load_dotenv()

# Parametry połączenia
database_password = os.environ.get('DATABASE_PASSWORD')
suszi_login = 'mkuzyk'
server = 'morfeusz.wszib.edu.pl'
driver = 'ODBC+Driver+18+for+SQL+Server'

# Tworzenie silnika bazy danych
engine = create_engine(
    f'mssql+pyodbc://{suszi_login}:{database_password}@{server}/{suszi_login}?driver={driver}&Encrypt=no',
    echo=False
)

Session = sessionmaker(bind=engine)

if __name__ == '__main__':
    session = Session()
    #session.execute(CreateSchema('Products'))
    #session.commit()

    # Importujemy Base i tworzymy tabele na podstawie metadanych
    from Alchemy_ORM.Laboratorium_4 import Base

    Base.metadata.create_all(engine)

    # Zatwierdzamy zmiany i zamykamy sesję
    session.commit()
    session.close()

Session = sessionmaker(engine)

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Wczytanie zmiennych środowiskowych
load_dotenv()

# Parametry połączenia
database_password = os.environ.get('DATABASE_PASSWORD')
suszi_login = 'mkuzyk'
server = 'morfeusz.wszib.edu.pl'
driver = 'ODBC+Driver+17+for+SQL+Server'

# Tworzenie silnika bazy danych
engine = create_engine(
    f'mssql+pyodbc://{suszi_login}:{database_password}@{server}/{suszi_login}?driver={driver}&Encrypt=no',
    echo=False
)

Session = sessionmaker(bind=engine)

# Tworzenie schematów i tabel w bazie
if __name__ == '__main__':
    session = Session()

    # Sprawdzamy, czy schemat istnieje, jeśli nie to go tworzymy
    check_schema_exists = text("""
        IF NOT EXISTS (SELECT * FROM sys.schemas WHERE name = 'Products')
        BEGIN
            EXEC('CREATE SCHEMA Products')
        END
    """)

    # Wykonujemy zapytanie warunkowe, które sprawdza, czy schemat istnieje, a jeśli nie, to go tworzy
    session.execute(check_schema_exists)

    # Importujemy Base i tworzymy tabele na podstawie metadanych
    from AlchemyORM.Laboratorium_4 import Base

    # Tworzenie tabel w schemacie Products
    Base.metadata.create_all(engine)

    # Zatwierdzamy zmiany i zamykamy sesję
    session.commit()
    session.close()
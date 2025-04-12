import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Table, MetaData, Column, String, Integer, Date, ForeignKey, func, select
from sqlalchemy.orm import sessionmaker

# Załaduj zmienne środowiskowe z pliku .env
load_dotenv()

# Pobierz hasło z pliku .env
database_password = os.environ.get('DATABASE_PASSWORD')
suszi_login = 'mkuzyk'
server = 'morfeusz.wszib.edu.pl'
driver = 'ODBC+Driver+17+for+SQL+Server'

# Połączenie z bazą danych MSSQL
engine = create_engine(
    f'mssql+pyodbc://{suszi_login}:{database_password}@{server}/{suszi_login}?driver={driver}&Encrypt=no',
    echo=False
)

# Definicja metadanych
metadata = MetaData()

# Tabela pracowników
worker_table = Table('workers', metadata,
                     Column('pesel', String(11), primary_key=True),
                     Column('first_name', String(255), nullable=False),
                     Column('last_name', String(255), nullable=False),
                     Column('birthday', Date, nullable=False),
                     Column('address_id', Integer, ForeignKey('address.address_id'), nullable=False),
                     )

# Tabela adresów
address_table = Table('address', metadata,
                     Column('address_id', Integer, primary_key=True, autoincrement=True),
                     Column('country', String(255), nullable=False),
                     Column('city', String(255), nullable=False),
                     Column('street', String(255), nullable=False),
                     Column('postal_code', String(25), nullable=False),
                     )

# Tworzymy połączenie z bazą danych
connection = engine.connect()

# Zapytanie: Liczba pracowników mieszkających w danym mieście
if __name__ == '__main__':
    query = select([address_table.c.city, func.count(worker_table.c.pesel).label('liczba_pracownikow')]) \
        .select_from(worker_table.join(address_table, worker_table.c.address_id == address_table.c.address_id)) \
        .group_by(address_table.c.city)

    # Wykonanie zapytania i wyświetlenie wyników
    result = connection.execute(query)
    for row in result:
        print(f"Miasto: {row['city']}, Liczba pracowników: {row['liczba_pracownikow']}")

# Zamknięcie połączenia
connection.close()

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData, select

load_dotenv()

# Dane do logowania
database_password = os.environ.get('DATABASE_PASSWORD')
suszi_login = 'mkuzyk'
server = 'morfeusz.wszib.edu.pl'
driver = 'ODBC+Driver+17+for+SQL+Server'

# Tworzenie silnika
engine = create_engine(
    f'mssql+pyodbc://{suszi_login}:{database_password}@{server}/{suszi_login}?driver={driver}&Encrypt=no',
    echo=False
)

# Automatyczne wczytanie struktury bazy danych
metadata = MetaData()
metadata.reflect(bind=engine)

# Wypisz wszystkie załadowane tabele
# print("Tabele w bazie:", metadata.tables.keys())

# Dostęp do konkretnych tabel
workers = metadata.tables['workers']
address = metadata.tables['address']

connection = engine.connect()

if __name__ == '__main__':
    query = select(workers.c.pesel,address.c.country)\
        .join_from (workers,address)
    result = connection.execute(query)
    print(result.fetchall())

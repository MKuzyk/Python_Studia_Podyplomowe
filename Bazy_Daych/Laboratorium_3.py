'''
1. Proszę napisać zapytania z wykorzystaniem SQL Alchemy Core
a. [0.2] Wszystkie adresy znajdujące się w Warszawie. Pobierz kolumny: Kraj, Miasto.
b. [0.2] Wszyscy pracownicy posortowani po dacie urodzenia w sposób malejący.
c. [0.2] Wszyscy pracownicy których imię zaczyna się na literę A lub M. Pobierz tylko
kolumny: Imię, Nazwisko.
d. [0.2] Wszyscy pracownicy którzy mieszkają w Warszawie.
e. [0.2] Liczbę pracowników mieszkających w danym mieście.
'''


import os

from dotenv import load_dotenv
from sqlalchemy import *
from sqlalchemy import create_engine

load_dotenv()

database_password = os.environ.get('DATABASE_PASSWORD')
suszi_login = 'mkuzyk'
server = 'morfeusz.wszib.edu.pl'
driver = 'ODBC+Driver+17+for+SQL+Server'

# dialect+driver://username:password@host:port/database?dodtkowe_opcje_klucz_wartość
engine = create_engine(
    f'mssql+pyodbc://{suszi_login}:{database_password}@{server}/{suszi_login}?driver={driver}&Encrypt=no',
    echo=False
)

metadata = MetaData()

worker_table = Table('workers', metadata,
                     Column('pesel', String(11), primary_key=True),
                     Column('first_name', String(255), nullable=False),
                     Column('last_name', String(255), nullable=False),
                     Column('birthday', Date, nullable=False),
                     Column('address_id', Integer,ForeignKey('address.address_id'), nullable=False),
                     )

address_table = Table('address', metadata,
                     Column('address_id', Integer, primary_key=True,autoincrement=True),
                     Column('country', String(255), nullable=False),
                     Column('city', String(255), nullable=False),
                     Column('street', String(255), nullable=False),
                     Column('postal_code', String(25), nullable=False),
                     )

connection = engine.connect()

'''
1. Proszę napisać zapytania z wykorzystaniem SQL Alchemy Core
a. [0.2] Wszystkie adresy znajdujące się w Warszawie. Pobierz kolumny: Kraj, Miasto.
'''

if __name__ == '__main__':
    query = select(address_table.c.country, address_table.c.city)\
        .where(address_table.c.city == 'Warszawa')
    result = connection.execute(query)
    print(result.fetchall())

'''
1. Proszę napisać zapytania z wykorzystaniem SQL Alchemy Core
b. [0.2] Wszyscy pracownicy posortowani po dacie urodzenia w sposób malejący.
'''

if __name__ == '__main__':
    query = select(worker_table).order_by(desc(worker_table.c.birthday))
    result = connection.execute(query)
    print(result.fetchall())

'''
1. Proszę napisać zapytania z wykorzystaniem SQL Alchemy Core
c. [0.2] Wszyscy pracownicy których imię zaczyna się na literę A lub M. Pobierz tylko
kolumny: Imię, Nazwisko.
'''

if __name__ == '__main__':
    query = select(worker_table.c.first_name, worker_table.c.last_name)\
        .where(or_(
            worker_table.c.first_name.like('A%'),  # Imiona zaczynające się na "A"
            worker_table.c.first_name.like('M%')   # Imiona zaczynające się na "M"
        ))

    result = connection.execute(query)
    print(result.fetchall())

'''
1. Proszę napisać zapytania z wykorzystaniem SQL Alchemy Core
d. [0.2] Wszyscy pracownicy którzy mieszkają w Warszawie.
e. [0.2] Liczbę pracowników mieszkających w danym mieście.
'''

if __name__ == '__main__':
    query = select(worker_table.join(address_table, worker_table.c.address_id == address_table.c.address_id)) \
        .where(address_table.c.city == 'Warszawa')
    result = connection.execute(query)
    print(result.fetchall())

'''
1. Proszę napisać zapytania z wykorzystaniem SQL Alchemy Core
e. [0.2] Liczbę pracowników mieszkających w danym mieście.
'''
if __name__ == '__main__':
    query = select(worker_table.join(address_table, worker_table.c.address_id == address_table.c.address_id))
    result = connection.execute(query)
    print(result.fetchall())

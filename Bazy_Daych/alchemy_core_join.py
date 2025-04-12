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
if __name__ == '__main__':
    query = select(worker_table.c.pesel,address_table.c.country)\
        .join_from (worker_table,address_table)
    result = connection.execute(query)
    print(result.fetchall())



if __name__ == '__main__':
    # Alias
    w = worker_table.alias()
    a = address_table.alias()

    query = select(worker_table, address_table.c.country) \
        .join_from(worker_table,address_table) \
        .where(worker_table.c.last_name == 'Kozłowski')
    result = connection.execute(query)
    print(result.fetchall())
'''

if __name__ == '__main__':
    query = (
        select(
            func.year(worker_table.c.birthday).label('rok'),
            address_table.c.city,
            func.count().label('liczba_urodzonych')
        )
        .select_from(worker_table.join(address_table, worker_table.c.address_id == address_table.c.address_id, isouter=True))  # LEFT JOIN
        .where(address_table.c.city == 'Kraków')
        .group_by(func.year(worker_table.c.birthday), address_table.c.city)
        .having(func.count() > 1)
        .order_by('liczba_urodzonych')
    )

    result = connection.execute(query)
    for row in result.fetchall():
        print(row)

#insert
if __name__ == '__main__':

    insert_sql=insert(address_table)\
        .values(country='Polska',city='Kraków',street='Aleja Kijowska',postal_code='30-390')
    connection.execute(insert_sql)
    connection.commit()

#insert many
if __name__ == '__main__':
    # Wstawianie wielu rekordów
    insert_many = insert(worker_table)
    values = [
        {'pesel': '11111111111', 'first_name': 'Marcin', 'last_name': 'Kuzyk', 'birthday': '2000-06-06',
             'address_id': 11},
        {'pesel': '99999999999', 'first_name': 'Marcin', 'last_name': 'Kasprzyk', 'birthday': '2001-06-06',
         'address_id': 12}
        ]
    connection.execute(insert_many, values)
    connection.commit()

# Update rekordów
if __name__ == '__main__':
    update_sql = update(worker_table).values(first_name='Zmienione').where(worker_table.c.address_id == 11)
    connection.execute(update_sql)
    connection.commit()

if __name__ == '__main__':
    delete_sql = delete(worker_table).where(worker_table.c.address_id == 11)
    connection.execute(delete_sql)
    connection.commit()

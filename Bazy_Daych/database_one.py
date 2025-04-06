import pyodbc
import os
from dotenv import load_dotenv
from pyodbc import drivers

load_dotenv()

db_password = os.environ.get('DB_PASSWORD')
sushi_login = 'mkuzyk'
server = 'morfeusz.wszib.edu.pl'

connection_string = (
    'DRIVER={ODBC Driver 17 for SQL Server};'
    f'SERVER={server};'
    f'DATABASE={sushi_login};'
    f'UID={sushi_login};'
    f'PWD={db_password};'
    'Encrypt=no'
)

connection = pyodbc.connect(connection_string)
'''
connection.execute("CREATE TABLE users(ID int identity, name varchar(255),age int)")
connection.execute("Insert into users(name,age) values('Michal',40),('Andrzej',28)")
connection.commit()
'''

#connection.execute("Insert into users(name,age) values('Jan',40),('Wojcieh',28)")
#connection.commit()

cursor=connection.cursor()

nowe_imie = input('Podaj nowe imię: ')


cursor.execute(f"Update users set name='{nowe_imie}' where name ='Nowe'")
connection.commit()

print(f'{cursor.rowcount} wierszy zmienionych')

cursor.execute("Select name from users")



for row in cursor:
    print(row[0])

cursor.close()
connection.close()

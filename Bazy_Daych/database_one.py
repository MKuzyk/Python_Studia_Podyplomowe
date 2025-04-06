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

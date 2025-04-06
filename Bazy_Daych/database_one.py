import pyodbc
import os
from dotenv import load_dotenv
load_dotenv()

print(os.environ.get('DB_PASSWORD'))
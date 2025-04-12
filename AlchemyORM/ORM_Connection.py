import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import CreateSchema
from alchemy_orm import Base

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

Session = sessionmaker(engine)

if __name__ == '__main__':
    session = Session()
    session.execute(CreateSchema('library_orm'))
    session.commit()
    Base.metadata.create_all(engine)

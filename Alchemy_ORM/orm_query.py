from ORM_Connection import Session
from sqlalchemy import *
from AlchemyORM.alchemy_orm import Author, Address, Book
from sqlalchemy.orm import joinedload
import datetime

session = Session()

select_authors = select(Author).options(joinedload(Author.books),joinedload(Author.address)).where(Author.id>1)
a = session.execute(select_authors).unique().scalars().all()

for author in a:
    print(f"Author {author.name} napisał {len(author.books)} książek i mieszka w {author.address.country}, {author.address.city}")

#Insert
# Dodawanie nowego autora
author = Author(name='Andrzej', email='email', login='login', middle_name='middle')

# Dodanie adresu
author.address = Address(country='Litwa', city='Wilno')

# Dodanie książki
book = Book(title='Jeden', publication_date=datetime.date.today())
author.books = [book]  # Przypisanie książki do autora

# Dodanie do sesji
session.add(author)  # Automatycznie doda książki i adres (relacje są załadowane)

# Zapisanie w bazie
session.commit()



'''
Zaprojektuj klasę produktu sklepu internetowego wg wytycznych:
• stwórz klasę o nazwie Product,
• dodaj (prywatne) właściwości jak nazwa, kategoria, cena, rabat w procentach,
• dodaj metodę obliczającą cenę uwzględniającą rabat,
• dodaj metodę sprawdzającą przynależność produktu do danej kategorii,
• dodaj metodę reprezentującą obiekt klasy jako ciąg znaków.
Dodatkowo stwórz grupę produktów z kilku kategorii, ustaw rabat dla produktów z jednej
kategorii i wyświetl listę produktów.
'''
from unicodedata import category


class Product:
    def __init__(self, name,category, price):
        self.__name = name
        self.__category = category
        self.__price = price
        self.__discount_in_percent = 0

    def set_discount_in_percent(self,percent):
        self.__discount_in_percent = percent

    def get_price_with_discount(self):
        result = (1-self.__discount_in_percent/100) * self.__price
        return round(result,2)

    def is_category(self,category):
        return self.__category==category

    def __str__(self):
        return f'{self.__name} ({self.__category}) - {self.get_price_with_discount()} zł'

def show_products(products):
    for product in products:
        print(product)

def special_offer(products,category,discount_in_percent):
    for product in products:
         if product.is_category(category):
             product.set_discount_in_percent(discount_in_percent)

products=[]

products.append(Product("mleko","spożywcze",3.99))
products.append(Product("masło","spożywcze",9))
products.append(Product("jogurt","spożywcze",4))
products.append(Product("kurczak","drób",14.5))
products.append(Product("płyn do naczyń","chemia",4.5))

show_products(products)
special_offer(products,"spożywcze",50)
print("\n PROMOCJA!")
show_products(products)
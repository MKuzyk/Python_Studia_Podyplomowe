from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

# Tworzenie bazy
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'schema': 'Products'}

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    middle_name = Column(String, nullable=True)

    # Relacje
    shipping_address = relationship("ShippingAddress", back_populates="user", uselist=False)
    carts = relationship("Cart", back_populates="user")

class ShippingAddress(Base):
    __tablename__ = 'shipping_addresses'
    __table_args__ = {'schema': 'Products'}

    id = Column(Integer, primary_key=True)
    country = Column(String)
    city = Column(String)
    postal_code = Column(String)
    block_number = Column(String)
    apartment_number = Column(String, nullable=True)

    # Relacja z użytkownikiem
    user_id = Column(Integer, ForeignKey('Products.users.id'))
    user = relationship("User", back_populates="shipping_address")

class Cart(Base):
    __tablename__ = 'carts'
    __table_args__ = {'schema': 'Products'}

    id = Column(Integer, primary_key=True)
    creation_date = Column(String)

    # Relacja z użytkownikiem
    user_id = Column(Integer, ForeignKey('Products.users.id'))
    user = relationship("User", back_populates="carts")

    # Relacja wiele do wielu z produktami
    products = relationship("Product", secondary="cart_products")

class Product(Base):
    __tablename__ = 'products'
    __table_args__ = {'schema': 'Products'}

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    price = Column(Integer)

class CartProduct(Base):
    __tablename__ = 'cart_products'
    __table_args__ = {'schema': 'Products'}

    cart_id = Column(Integer, ForeignKey('Products.carts.id'), primary_key=True)
    product_id = Column(Integer, ForeignKey('Products.products.id'), primary_key=True)
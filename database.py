from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Настройка подключения к базе данных
DATABASE_URL = "postgresql://postgres:123@localhost:5432/postgres"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Определение базовой модели
Base = declarative_base()

# Модель для таблицы Address
class Address(Base):
    __tablename__ = 'address'

    id_address = Column(Integer, primary_key=True)
    index = Column(Integer)
    region = Column(String(100))
    country = Column(String(100))
    street = Column(String(100))
    house = Column(Integer)

# Модель для таблицы TypePartner
class TypePartner(Base):
    __tablename__ = 'type_partners'

    id_type_partners = Column(Integer, primary_key=True)
    type_partners = Column(String(100))

# Модель для таблицы Partner
class Partner(Base):
    __tablename__ = 'partners'

    id_partners = Column(Integer, primary_key=True)
    type_partners = Column(Integer, ForeignKey('type_partners.id_type_partners'))
    name_partners = Column(String(200))
    director = Column(String(200))
    phone = Column(String(10))
    email = Column(String(40))
    rating = Column(Integer)
    address = Column(Integer, ForeignKey('address.id_address'))

    # Связи
    type_partner = relationship("TypePartner", backref="partners")
    address_rel = relationship("Address", backref="partners")

# Модель для таблицы Product (Продукция)
class Products(Base):
    __tablename__ = 'products'

    id_product = Column(Integer, primary_key=True)
    type_product = Column(Integer, ForeignKey('type_product.id_type_product'))
    name_product = Column(String(200))
    article = Column(String(7))
    price = Column(Float)
    size = Column(Float)
    classs = Column(Integer) 

    # Связи
    type_product_rel = relationship("TypeProduct", backref="products")

# Модель для таблицы TypeProduct
class TypeProduct(Base):
    __tablename__ = 'type_product'

    id_type_product = Column(Integer, primary_key=True)
    type_product = Column(String(100))
    ratio = Column(Float)

# Модель для таблицы Materials
class Materials(Base):
    __tablename__ = 'materials'

    id_materials = Column(Integer, primary_key=True)
    type_materials = Column(String(100))
    marriage = Column(Float)

# Модель для таблицы MaterialProduct
class MaterialProduct(Base):
    __tablename__ = 'material_product'

    id_material_product = Column(Integer, primary_key=True)
    product = Column(Integer, ForeignKey('products.id_product'))
    material = Column(Integer, ForeignKey('materials.id_materials'))

# Модель для таблицы PartnerProduct
class PartnerProduct(Base):
    __tablename__ = 'partner_product'

    id_partner_product = Column(Integer, primary_key=True)
    product = Column(Integer, ForeignKey('products.id_product'))
    id_partner = Column(Integer, ForeignKey('partners.id_partners'))
    count_product = Column(Integer)
    date_sale = Column(String)  

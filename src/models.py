from sqlalchemy import Column, String, Text, Float, DateTime, Integer, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from fastapi_storages.integrations.sqlalchemy import FileType
from app import product_image_storage
from db import Base


class ProductType(Base):
    __tablename__ = "product_type"
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    description = Column(Text())
    products = relationship("Product", back_populates="product_type")
    created_at = Column(DateTime, server_default=func.now())  # дата создания
    updated_at = Column(DateTime, onupdate=func.now())  # дата обновления

    def __repr__(self):
        return (
            f"<Название: {self.name}, материал: {self.description}>")


class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True)
    product_image = Column(FileType(storage=product_image_storage))  # адрес картинки
    name = Column(String(200))  # название товара\
    description = Column(Text())  # описание товара
    material = Column(String(100))  # материал
    price = Column(Float(10))  # цена
    length = Column(String(50))  # длина
    color = Column(String(50))  # цвет
    width = Column(String(50))  # ширина
    size = Column(String(100))  # размеры
    url = Column(String(250))  # ссылка на товар АВИТО
    product_type_id = Column(Integer, ForeignKey("product_type.id"))
    categories = relationship("Category", secondary="product2category")
    product_type = relationship("ProductType", back_populates="products")
    created_at = Column(DateTime, server_default=func.now())  # дата создания
    updated_at = Column(DateTime, onupdate=func.now())  # дата обновления
    def get_image_url(self):
        return str(self.product_image).replace('..','')


    def __repr__(self):
        return (
            f"<Название: {self.name}, материал: {self.material}, "
            f"цвет: {self.color}, цена: {self.price}>")


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))  # название
    description = Column(Text())  # описание
    products = relationship("Product", secondary="product2category")
    created_at = Column(DateTime, server_default=func.now())  # дата создания
    updated_at = Column(DateTime, onupdate=func.now())  # дата обновления

    def __repr__(self):
        return (f"< название: {self.name}>")


class Product2Category(Base):
    __tablename__ = "product2category"
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("product.id"))
    category_id = Column(Integer, ForeignKey("category.id"))


class DescriptText(Base):
    __tablename__ = "descript_text"
    id = Column(Integer, primary_key=True)
    description = Column(Text())  # описание сайта
    email = Column(String(100))  # почта для контакта
    telephone = Column(String(50))  # телефон для контакта
    link_1 = Column(String(250))  # ссылка для вставки 1
    link_2 = Column(String(250))  # ссылка для вставки 2
    created_at = Column(DateTime, server_default=func.now())  # дата создания
    updated_at = Column(DateTime, onupdate=func.now())  # дата обновления


from sqlalchemy import Column, String, Text, Float, DateTime, Integer
from sqlalchemy.sql import func

from db import Base


# класс с ремнями
class Belts(Base):
    __tablename__ = "belts"
    id = Column(Integer, primary_key=True)

    name = Column(String(200))  # название товара
    description = Column(Text())  # описание товара
    material = Column(String(100))  # материал
    length = Column(String(50))  # длина
    color = Column(String(50))  # цвет
    width = Column(String(50))  # ширина
    price = Column(Float(10))  # цена

    created_at = Column(DateTime, server_default=func.now())  # дата создания
    updated_at = Column(DateTime, server_onupdate=func.now())  # дата обновления

    def __repr__(self):
        return(f"<Название: {self.name}, материал: {self.material}, цвет: {self.color}, цена: {self.price}>")



# класс с пряжками
class Buckles(Base):
    __tablename__ = "buckles"
    id = Column(Integer, primary_key=True)

    name = Column(String(200))  # название товара
    description = Column(Text())  # описание товара
    material = Column(String(100))  # материал
    size = Column(String(100))  # размеры
    color = Column(String(50))  # цвет
    price = Column(Float(10))  # цена

    created_at = Column(DateTime, server_default=func.now())  # дата создания
    updated_at = Column(DateTime, server_default=func.now())  # дата обновления

    def __repr__(self):
        return (f"<Название: {self.name}, материал: {self.material}, цвет: {self.color}, цена: {self.price}>")


#  класс Портмоне
class Purse(Base):
    __tablename__ = "purse"
    id = Column(Integer, primary_key=True)

    name = Column(String(200))  # название товара
    description = Column(Text())  # описание товара
    material = Column(String(100))  # материал
    size = Column(String(100))  # размеры
    color = Column(String(50))  # цвет
    price = Column(Float(10))  # цена

    created_at = Column(DateTime, server_default=func.now())  # дата создания
    updated_at = Column(DateTime, server_default=func.now())  # дата обновления

    def __repr__(self):
        return (f"<Название: {self.name}, материал: {self.material}, цвет: {self.color}, цена: {self.price}>")

# класс кошельки
class Wallets(Base):
    __tablename__ = "wallets"
    id = Column(Integer, primary_key=True)

    name = Column(String(200))  # название товара
    description = Column(Text())  # описание товара
    material = Column(String(100))  # материал
    size = Column(String(100))  # размеры
    color = Column(String(50))  # цвет
    price = Column(Float(10))  # цена


#  класс картхолдеры
class Cartholders(Base):
    __tablename__ = "cartholders"
    id = Column(Integer, primary_key=True)

    name = Column(String(200))  # название товара
    description = Column(Text())  # описание товара
    material = Column(String(100))  # материал
    size = Column(String(100))  # размеры
    color = Column(String(50))  # цвет
    price = Column(Float(10))  # цена

    created_at = Column(DateTime, server_default=func.now())  # дата создания
    updated_at = Column(DateTime, server_default=func.now())  # дата обновления

    def __repr__(self):
        return (f"<Название: {self.name}, материал: {self.material}, цвет: {self.color}, цена: {self.price}>")


# класс стельки
class Insoles(Base):
    __tablename__ = "insoles"
    id = Column(Integer, primary_key=True)

    name = Column(String(200))  # название товара
    description = Column(Text())  # описание товара
    material = Column(String(100))  # материал
    size = Column(String(100))  # размеры
    color = Column(String(50))  # цвет
    price = Column(Float(10))  # цена

    created_at = Column(DateTime, server_default=func.now())  # дата создания
    updated_at = Column(DateTime, server_default=func.now())  # дата обновления

    def __repr__(self):
        return (f"<Название: {self.name}, материал: {self.material}, цвет: {self.color}, цена: {self.price}>")

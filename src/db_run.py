from models import Belts, Buckles, Purse, Wallets, Cartholders, Insoles
from os import remove
from db import SessionLocal, Base, engine

Base.metadata.create_all(engine, checkfirst=True)
db = SessionLocal()  # создание соединения с БД

belts = Belts(name="ремень тактический", description="хороший ремень для военного", material="брезент",  # ремни
              length="100 см.", color="зеленый", width="5 см.", price=750.00)

belts_1 = Belts(name="ремень кожанный", description="стильный ремень для мужчины", material="кожа носорога",  # ремни
              length="100 см.", color="черный", width="5 см.", price=750.00)

belts_2 = Belts(name="ремень элегантный", description="ремень для гламурного дяденьки", material="крепдышин",  # ремни
              length="100 см.", color="синий", width="5 см.", price=750.00)

belts_3 = Belts(name="ремень красивый", description="ремень для пальто", material="кошемир",  # ремни
              length="100 см.", color="черный", width="5 см.", price=750.00)

belts_4 = Belts(name="ремень блестящий", description="ремень для блестящей куртки", material="полипропилен",  # ремни
              length="100 см.", color="стальной", width="5 см.", price=750.00)

belts_5 = Belts(name="ремень практичныйй", description="крепкий ремень из толстой кожи", material="кожа",  # ремни
              length="100 см.", color="черный", width="5 см.", price=750.00)

buckles = Buckles(name="пряжка СССР", description="пряжка для ремня", material="железо",   # пряжки
              size="5 х 4 см.", color="Стального", price=350.00)

buckles_1 = Buckles(name="пряжка со звездой", description="пряжка для ремня", material="железо",    # пряжки
              size="5 х 4 см.", color="черного", price=350.00)

purse = Purse(name="портмоне", description="удобный портмоне из России", material="кожа",   # портмоне
              size="5 х 4 см.", color="Стального", price=2350.00)

purse_1 = Purse(name="портмоне", description="удобный портмоне из России", material="экокожа",    # портмоне
              size="5 х 4 см.", color="белого", price=850.00)

db.add_all([belts, belts_1, buckles, buckles_1, purse, purse_1])
db.commit()

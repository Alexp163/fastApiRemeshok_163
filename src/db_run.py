from models import Belts, Buckles, Purse, Wallets, Cartholders, Insoles
from os import remove
from db import SessionLocal, Base, engine

Base.metadata.create_all(engine, checkfirst=True)
db = SessionLocal()  # создание соединения с БД

belts = Belts(name="ремень тактический", description="хороший ремень для военного", material="брезент",
              length="100 см.", color="зеленый", width="5 см.", price=750.00)

belts_1 = Belts(name="ремень тактический", description="хороший ремень для военного", material="брезент",
              length="100 см.", color="зеленый", width="5 см.", price=750.00)
db.add_all([belts, belts_1])
db.commit()

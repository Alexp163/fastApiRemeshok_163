from models import Product
from db import SessionLocal
from pprint import pprint

db = SessionLocal()
products = db.query(Product).all()
pprint(products)






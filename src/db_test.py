from models import Product, Category
from db import SessionLocal
from pprint import pprint

db = SessionLocal()

categories = db.query(Category).all()
for category in categories:
    print("====", category.name)
    for product in category.products:
        pprint(product)








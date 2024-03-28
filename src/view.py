from fastapi import Request
from db import SessionLocal
from app import app
from templates import render_template
from tools import make_product_groups, make_categories_groups
from models import Product, ProductType, Category, DescriptText


@app.get("/")
async def index(request: Request):
    db = SessionLocal()
    product_types = db.query(ProductType).all()
    categories = db.query(Category).all()
    categories = make_categories_groups(categories, 4)
    descript_text = db.query(DescriptText).first()
    return render_template("index.html", request=request,
                           product_types=product_types, categories=categories,
                           descript_text=descript_text)


@app.get("/single")
def single(request: Request):
    return render_template("single.html", request=request)


@app.get("/purse")
def purse(request: Request):
    return render_template("purse.html", request=request)


@app.get("/products_by_type/{product_type_id}")
def products_by_type(request: Request, product_type_id: int):
    db = SessionLocal()
    products = db.query(Product).filter_by(product_type_id=product_type_id)
    product_groups = make_product_groups(products, 4)
    return render_template("products.html", request=request,
                           product_groups=product_groups)


@app.get("/products")
def products(request: Request):
    db = SessionLocal()
    products = db.query(Product).all()
    product_groups = make_product_groups(products, 4)
    return render_template("products.html", request=request,
                           product_groups=product_groups)


@app.get("/about_us")
def about_us(request: Request):
    return render_template("about_us.html", request=request)


@app.get("/contacts")
def contacts(request: Request):
    return render_template("contacts.html", request=request)

@app.get("/single/{product_id}")
def single(request: Request, product_id: int):
    db = SessionLocal()
    product = db.query(Product).get(product_id)
    return render_template("single.html", request=request, product=product)




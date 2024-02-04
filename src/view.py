from fastapi import Request

from app import app
from templates import render_template


@app.get("/")
async def index(request: Request):
    return render_template("index.html", request=request)

@app.get("/single")
def single(request: Request):
    return render_template("single.html", request=request)


@app.get("/purse")
def purse(request: Request):
    return render_template("purse.html", request=request)


@app.get("/belts")
def belts(request: Request):
    return render_template("belts.html", request=request)


@app.get("/products")
def products(request: Request):
    return render_template("products.html", request=request)


@app.get("/about_us")
def about_us(request: Request):
    return render_template("about_us.html", request=request)


@app.get("/contacts")
def contacts(request: Request):
    return render_template("contacts.html", request=request)

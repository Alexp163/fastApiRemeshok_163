from sqladmin import Admin
from sqladmin import ModelView

from app import app
from db import engine
from models import Product, Category, ProductType, DescriptText
from fastapi import Request
from sqladmin.authentication import AuthenticationBackend


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        """Функция, проверяющая данные в форме авторизации"""

        form = await request.form()
        username, password = form["username"], form["password"]
        if username == "AlexAdmin" and password == "9502039Popov---":
            request.session.update({"token": "1234"})
            return True
        else:
            return False

    async def logout(self, request: Request) -> bool:
        """Функция, проверяющая был ли авторизован пользователь"""
        request.session.clear()

    async def authenticate(self, request: Request) -> bool:
        """Функция, проверяющая был ли авторизован пользователь"""

        token = request.session.get("token")

        if token is not None and token == "1234":
            return True
        else:
            return False

sqladmin = AdminAuth(secret_key="09485u42[w5lkjkjk")
admin = Admin(app, engine, authentication_backend=sqladmin)



class ProductsModelView(ModelView, model=Product):
    column_list = [Product.name, Product.description, Product.price, Product.material, Product.color]
    form_excluded_columns = [Product.created_at, Product.updated_at]


class CategoryModelView(ModelView, model=Category):
    column_list = [Category.id, Category.name, Category.description]
    form_excluded_columns = [Category.created_at, Category.updated_at]


class ProductTypeModelView(ModelView, model=ProductType):
    column_list = [ProductType.id, ProductType.name, ProductType.description]
    form_excluded_columns = (ProductType.created_at, ProductType.updated_at)

class DescriptTextModelView(ModelView, model=DescriptText):
    column_list = [DescriptText.id, DescriptText.description, DescriptText.email,
                   DescriptText.telephone,
                   DescriptText.link_1, DescriptText.link_2]
    form_excluded_columns = (DescriptText.created_at, DescriptText.updated_at)


admin.add_view(CategoryModelView)
admin.add_view(ProductsModelView)
admin.add_view(ProductTypeModelView)
admin.add_view(DescriptTextModelView)


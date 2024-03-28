from sqladmin import Admin
from sqladmin import ModelView

from app import app
from db import engine
from models import Product, Category, ProductType, DescriptText

admin = Admin(app, engine)


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



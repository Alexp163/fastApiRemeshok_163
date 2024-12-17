from fastapi import FastAPI
from fastapi_storages import FileSystemStorage

product_image_storage = FileSystemStorage(path="../static/images/products")

app = FastAPI()

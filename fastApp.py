from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

database = []

class Product(BaseModel):
    title: str
    quantity: int
    price: float
    inStock: bool

@app.post("/createItem/")
def create_item_endpoint(product:Product):
    database.append({
        "id": random.randint(0-999),
        "title": product.title,
        "quantity": product.quantity,
        "price": product.price,
        "inStock": product.inStock

    })
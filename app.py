from fastapi import FastAPI
from pydantic import BaseModel
import random 

# pip3 install uvicorn 
# pip3 install fastapi

# uvicorn file_name:app_instance --reload
#


app = FastAPI()
database = []


class Product(BaseModel):
    title: str 
    quantity: int 
    price: float 
    inStock: bool 


@app.post("/createItem/")
def create_item_endpoint(product: Product): # if schema/submitted data is validated then it goes through to our logic in the function
    database.append({
        "id": random.randint(0, 999),
        "title": product.title,
        "quantity": product.quantity,
        "price": product.price,
        "inStock": product.inStock
    })

    return {
        "status": "product created", # a custom response field we added for style
        "dataAccepted": product # the data the user submitted to the endpoint
    }

@app.get("/products")
def get_products():
    return database

@app.delete("/delete/product/{product_id}")
def delete_product(product_id):
    for index, obj in enumerate(database):
        if obj['id'] == int(product_id):
            database.pop(index)
            break 

    return {
        "status": f"Product with ID {product_id} has been deleted"
    }


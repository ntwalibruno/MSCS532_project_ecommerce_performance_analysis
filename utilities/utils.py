import sys
import os
import json
from datetime import datetime

#Imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'models')))
from product import Product 

def load_products_from_json(filename):
    with open(filename, 'r') as file:
        products_data = json.load(file)
        products = []
        for product_data in products_data:
            product = Product(
                id=product_data['id'],
                product_type=product_data['product_type'],
                product_name=product_data['product_name'],
                comments_id=product_data['comments_id'],
                insert_date=product_data['insert_date'],
                creation_date=product_data['creation_date'],
                creator_id=product_data['creator_id']
            )
            products.append(product)
        return products

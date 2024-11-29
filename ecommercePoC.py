import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'models')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'algorithms')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'data')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'utilities')))

# print(sys.path)

from product import Product
from avl_tree import AVLTree
from utils import load_products_from_json  

prooductData = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/products.json'))
products = load_products_from_json(prooductData)

avl_tree = AVLTree()
avl_tree.insert_products(products)

my_product = Product(501, "Electronics", "Smartphone X200", 101, "2024-03-12T15:45:08.476653", "2023-08-25T07:53:22.746632", 502)

avl_tree.insert_product(my_product)

print(avl_tree.search_product(1).product)
print(avl_tree.search_product(400).product)
print(avl_tree.search_product(240).product)



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
from graph import CorrelationGraph

productData = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/products.json'))
products = load_products_from_json(productData)

#AVL Tree
avl_tree = AVLTree()
avl_tree.insert_products(products)

my_product = Product(501, "Electronics", "Smartphone X200", 101, "2024-03-12T15:45:08.476653", "2023-08-25T07:53:22.746632", 502)

avl_tree.insert_product(my_product)

print(avl_tree.search_product(1).product)
print(avl_tree.search_product(400).product)
print(avl_tree.search_product(240).product)

#Product correltaion graph
graph = CorrelationGraph(products)

# Create correlations
graph.correlate_by_type()
graph.correlate_by_creator()
graph.correlate_by_insert_date(time_window=5)

# Display the graph with correlations
# graph.display_graph()

top_correlated = graph.get_correlated_products(products[34], top_n=10)


# Display the top correlated products
print(products[34])
print("\n")
for p in top_correlated:
    print(f"Product ID {p.id}: {p.product_name} (Type: {p.product_type}, Creator: {p.creator_id})")
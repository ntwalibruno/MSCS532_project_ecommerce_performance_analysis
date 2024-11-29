import datetime
import time
import random
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../models')))

from product import Product
from avl_tree import AVLTree


# Generate random products
def generate_products(num_products):
    products = []
    for i in range(1, num_products + 1):
        product = Product(
            id=i,
            product_type="Type" + str(random.randint(1, 5)),
            product_name="Product" + str(i),
            comments_id=random.randint(1000, 9999),
            insert_date="2024-11-01",
            creation_date="2024-10-01",
            creator_id=random.randint(1, 10)
        )
        products.append(product)
    return products

# Function to test insertion, search, and deletion
def test_avl_tree_operations(tree, products, load_size):
    print(f"\nTesting with {load_size} products:")

    start_time = time.time()
    tree.insert_products(products)
    insertion_time = time.time() - start_time
    print(f"Insertion Time: {insertion_time:.6f} seconds")

    random_product = random.choice(products)
    start_time = time.time()
    tree.search_product(random_product.id)
    search_time = time.time() - start_time
    print(f"Search Time for product {random_product.id}: {search_time:.6f} seconds")

    start_time = time.time()
    tree.delete_product(random_product.id)
    deletion_time = time.time() - start_time
    print(f"Deletion Time for product {random_product.id}: {deletion_time:.6f} seconds")

# Run test on different load sizes
def run_progressive_tests():
    tree = AVLTree()
    load_sizes = [100, 500, 1000, 5000, 10000, 20000]  

    for load_size in load_sizes:
        products = generate_products(load_size)
        test_avl_tree_operations(tree, products, load_size)

# Run the tests
run_progressive_tests()

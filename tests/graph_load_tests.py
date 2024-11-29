import time
import random
import sys
import os
from datetime import datetime, timedelta

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../models')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../algorithms')))

from product import Product
from graph import CorrelationGraph

# Generate random products
def generate_products(num_products):
    products = []
    for i in range(1, num_products + 1):
        product = Product(
            id=i,
            product_type="Type" + str(random.randint(1, 5)),
            product_name="Product" + str(i),
            comments_id=random.randint(1000, 9999),
            insert_date=(datetime.now() - timedelta(days=random.randint(0, 365))).strftime("%Y-%m-%d"),
            creation_date=(datetime.now() - timedelta(days=random.randint(0, 365))).strftime("%Y-%m-%d"),
            creator_id=random.randint(1, 10)
        )
        products.append(product)
    return products

# Function to test correlation graph operations
def test_correlation_graph_operations(graph, products, load_size):
    print(f"\nTesting with {load_size} products:")

    start_time = time.time()
    graph.correlate_by_type()
    correlate_by_type_time = time.time() - start_time
    print(f"Correlation by Type Time: {correlate_by_type_time:.6f} seconds")

    start_time = time.time()
    graph.correlate_by_creator()
    correlate_by_creator_time = time.time() - start_time
    print(f"Correlation by Creator Time: {correlate_by_creator_time:.6f} seconds")

    start_time = time.time()
    graph.correlate_by_insert_date(time_window=30)
    correlate_by_insert_date_time = time.time() - start_time
    print(f"Correlation by Insert Date Time: {correlate_by_insert_date_time:.6f} seconds")

    random_product = random.choice(products)
    start_time = time.time()
    top_correlated_products = graph.get_correlated_products(random_product, top_n=10)
    top_correlated_products_time = time.time() - start_time
    print(f"Get Top 10 Correlated Products Time: {top_correlated_products_time:.6f} seconds")
    print(f"Top 10 Correlated Products for {random_product.id}: {[product.id for product in top_correlated_products]}")

# Test with progressively increasing load size
def run_progressive_tests():
    load_sizes = [100, 500, 1000, 5000, 10000]  

    for load_size in load_sizes:
        products = generate_products(load_size)
        graph = CorrelationGraph(products=products)
        test_correlation_graph_operations(graph, products, load_size)

# Run the tests
run_progressive_tests()

# Correlation Graph Project

## Project Overview
This project implements `CorrelationGraph` class that manages correlations between products based on their attributes such as type, creator, and insert date. The graph is represented using a dictionary where each product is a key, and the value is a list of correlated product IDs.

## Features
- Add products to the graph
- Correlate products by type, creator, and insert date
- Display the correlation graph
- Calculate correlation scores between products
- Retrieve top correlated products for a given product

## How to Run

### Prerequisites
- Python 3.x

### Installation
1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```


### Usage

### Tests
Project also include load tests for different load sizes.


## Example
```python
from datetime import datetime
from graph import CorrelationGraph

class Product:
    def __init__(self, id, product_type, creator_id, insert_date):
        self.id = id
        self.product_type = product_type
        self.creator_id = creator_id
        self.insert_date = insert_date

# Example products
products = [
    Product(1, 'TypeA', 'Creator1', datetime(2023, 1, 1)),
    Product(2, 'TypeA', 'Creator2', datetime(2023, 1, 15)),
    Product(3, 'TypeB', 'Creator1', datetime(2023, 2, 1)),
    Product(4, 'TypeA', 'Creator1', datetime(2023, 3, 1)),
]

# Initialize and populate the graph
graph = CorrelationGraph(products)
graph.correlate_by_type()
graph.correlate_by_creator()
graph.correlate_by_insert_date(time_window=30)

# Display the graph
graph.display_graph()

# Get top correlated products for a given product
product = products[0]
top_correlated_products = graph.get_correlated_products(product, top_n=2)
print(f"Top correlated products for {product.id}: {[p.id for p in top_correlated_products]}")
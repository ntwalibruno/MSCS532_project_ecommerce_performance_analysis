from collections import defaultdict

class CorrelationGraph:
    def __init__(self, products=None):
        # Initialize the graph as a defaultdict of lists
        self.graph = defaultdict(list)
        # Initialize the products dictionary
        self.products = {}
        
        # If a list of products is provided, populate the graph with them
        if products:
            self.populate_graph(products)

    def populate_graph(self, products):
        # Populate the products dictionary with the provided products
        for product in products:
            self.products[product.id] = product

    def add_correlation(self, product1, product2):
        # Add a correlation between product1 and product2
        if product2.id not in self.graph[product1.id]:
            self.graph[product1.id].append(product2.id)
        if product1.id not in self.graph[product2.id]:
            self.graph[product2.id].append(product1.id)

    def correlate_by_type(self):
        # Correlate products by their type
        for product1 in self.products.values():
            for product2 in self.products.values():
                if product1.id != product2.id and product1.product_type == product2.product_type:
                    self.add_correlation(product1, product2)

    def correlate_by_creator(self):
        # Correlate products by their creator
        for product1 in self.products.values():
            for product2 in self.products.values():
                if product1.id != product2.id and product1.creator_id == product2.creator_id:
                    self.add_correlation(product1, product2)

    def correlate_by_insert_date(self, time_window=30):
        # Correlate products by their insert date within a given time window
        for product1 in self.products.values():
            for product2 in self.products.values():
                if product1.id != product2.id:
                    time_diff = abs((product1.insert_date - product2.insert_date).days)
                    if time_diff <= time_window:
                        self.add_correlation(product1, product2)

    def display_graph(self):
        # Display the graph showing correlations between products
        for product_id, correlated_ids in self.graph.items():
            print(f"Product {product_id} is correlated with: {correlated_ids}")

    def get_correlation_score(self, product1, product2):
        # Calculate the correlation score between two products
        score = 0
        if product1.product_type == product2.product_type:
            score += 1
        if product1.creator_id == product2.creator_id:
            score += 1
        if abs((product1.insert_date - product2.insert_date).days) <= 30:
            score += 1
        return score

    def get_correlated_products(self, product, top_n=10):
        # Get the top_n correlated products for a given product
        correlations = []
        for other_product in self.products.values():
            if other_product.id != product.id:
                score = self.get_correlation_score(product, other_product)
                if score > 0:  
                    correlations.append((other_product, score))

        # Sort the correlations by score in descending order
        correlations.sort(key=lambda x: x[1], reverse=True)

        # Return the top_n products from the sorted correlations
        return [product for product, score in correlations[:top_n]]

class AVLNode:
    def __init__(self, product):
        self.product = product 
        self.left = None
        self.right = None
        self.height = 1  

class AVLTree:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        if node is None:
            return 0
        return node.height

    def get_balance_factor(self, node):
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1

        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1

        return y

    #Insert
    def insert(self, root, product):
        if root is None:
            return AVLNode(product)

        if product.id < root.product.id:
            root.left = self.insert(root.left, product)
        else:
            root.right = self.insert(root.right, product)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance_factor(root)

        if balance > 1 and product.id < root.left.product.id:
            return self.right_rotate(root)

        if balance < -1 and product.id > root.right.product.id:
            return self.left_rotate(root)

        if balance > 1 and product.id > root.left.product.id:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and product.id < root.right.product.id:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    #Search
    def search(self, root, product_id):
        if root is None or root.product.id == product_id:
            return root

        if product_id < root.product.id:
            return self.search(root.left, product_id)

        return self.search(root.right, product_id)

    # Delete 
    def delete(self, root, product_id):
        if root is None:
            return root

        if product_id < root.product.id:
            root.left = self.delete(root.left, product_id)
        elif product_id > root.product.id:
            root.right = self.delete(root.right, product_id)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            root.product = self.get_min_value_node(root.right).product

            root.right = self.delete(root.right, root.product.id)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance_factor(root)

        if balance > 1 and self.get_balance_factor(root.left) >= 0:
            return self.right_rotate(root)

        if balance < -1 and self.get_balance_factor(root.right) <= 0:
            return self.left_rotate(root)

        if balance > 1 and self.get_balance_factor(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and self.get_balance_factor(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def get_min_value_node(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current

    def insert_product(self, product):
        self.root = self.insert(self.root, product)

    def insert_products(self, prodcusts):
        for product in prodcusts:
            self.insert_product(product)

    def search_product(self, product_id):
        return self.search(self.root, product_id)

    def delete_product(self, product_id):
        self.root = self.delete(self.root, product_id)


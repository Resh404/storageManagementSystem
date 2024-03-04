class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def update_product_details(self, product_id, **kwargs):
        for product in self.products:
            if product.id == product_id:
                for key, value in kwargs.items():
                    setattr(product, key, value)
                break
        else:
            print("Product not found.")

    def get_product_details(self, product_id):
        for product in self.products:
            if product.id == product_id:
                return product
        print("Product not found.")

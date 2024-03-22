from productDefinition.product_imp import Product
from productUtils.Iproduct_handler_imp import ProductHandler

''' This class defines a inventory and what can be done to a inventory.
The class implements the ProductHandler interface which defines the bare minimum methods it need.
The initialized parameters defines what a inventory need to be initialized with.
The names of the methods explains the functionality of the method. '''


class Inventory(ProductHandler):
    def __init__(self):
        self.products = []

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            print("Invalid product")
            return
        self.products.append(product)

    def remove_product(self, product: Product) -> None:
        if product not in self.products:
            print("Product not found in the inventory.")
            return
        self.products.remove(product)

    def update_product_details(self, product_id, **kwargs) -> None:
        found_product = False
        for product in self.products:
            if product.id == product_id:
                found_product = True
                for key, value in kwargs.items():
                    setattr(product, key, value)
                break
        if not found_product:
            print("Product not found.")

    def get_product_details(self, product_id) -> Product:
        for product in self.products:
            if product.id == product_id:
                return product
        print("Product not found.")

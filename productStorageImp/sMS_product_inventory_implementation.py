from productCreationImp.sMS_product_implementation import Product
from productUtilsImp.sMS_Iproduct_handler_implementation import ProductHandler


class Inventory(ProductHandler):
    def __init__(self):
        self.products = []

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            print("Invalid product")
            return
        self.products.append(product)
        print("Product added.")

    def remove_product(self, product: Product) -> None:
        if product not in self.products:
            print("Product not found in the inventory.")
            return
        self.products.remove(product)
        print("Product removed.")

    def update_product_details(self, product_id, **kwargs) -> None:
        found_product = False
        for product in self.products:
            if product.id == product_id:
                found_product = True
                for key, value in kwargs.items():
                    setattr(product, key, value)
                    print("Product updated.")
                break
        if not found_product:
            print("Product not found.")

    def get_product_details(self, product_id) -> Product:
        for product in self.products:
            if product.id == product_id:
                return product
        print("Product not found.")

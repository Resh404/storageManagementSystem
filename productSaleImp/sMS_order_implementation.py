from typing import List
from productCreationImp.sMS_product_implementation import Product
from productStorageImp.sMS_product_warehouse_implementation import Warehouse
from productUtilsImp.sMS_Iproduct_handler_implementation import ProductHandler


class Order(ProductHandler):
    _reserved_products_list = []

    def __init__(self, id: int, products: List['Product']):
        self.id = id
        self.products = products

    def add_reserved_product(self, product: Product):
        self._reserved_products_list.append(product)

    def add_product(self, product: Product) -> None:
        self.products.append(product)

    def remove_product(self, product: Product) -> None:
        self.products.remove(product)

    def reserve_product_from_warehouse(self, product_ids: List[int], quantities: List[int],
                                       warehouse: Warehouse) -> bool:
        # I guess in a real application you would use product names?
        for prod_id, quantity in zip(product_ids, quantities):
            # Find the product in warehouse
            found = False
            for product in warehouse.products:
                if product.id == prod_id:
                    if product.quantity >= quantity:

                        reserved_product = Product(product.id, product.name, product.price, quantity, product.category)
                        self._reserved_products_list.append(reserved_product)
                        product.quantity -= quantity

                        # Check if the product needs to be removed from the warehouse
                        if product.quantity <= 0:
                            warehouse.remove_product(product)
                        found = True
                        break
                    else:
                        print(f"Desired quantity of product with ID {prod_id} not available")
                        return False
            if not found:
                print(f"Product ID {prod_id} not found in the warehouse")
                return False
        return True

from productDefinition.product_imp import Product
from productUtils.Iproduct_handler_imp import ProductHandler
from productStorage.product_warehouse_imp import Warehouse
from typing import List

''' This class defines a supplier and what can be done by a supplier.
The class implements the ProductHandler interface which defines the bare minimum methods it need.
The initialized parameters defines what a supplier need to be initialized with.
The names of the methods explains the functionality of the method. '''


class Supplier(ProductHandler):
    def __init__(self, id: int, name: str, contact_details: str, products_supplied: List['Product']):
        self.id = id
        self.name = name
        self.contact_details = contact_details
        self.products_supplied = products_supplied

    def add_product(self, product: Product) -> None:
        self.products_supplied.append(product)

    def remove_product(self, product: Product) -> None:
        self.products_supplied.remove(product)

    def deliver_supplies_to_warehouse(self, warehouse: Warehouse) -> None:
        i = 0

        for product in self.products_supplied:
            if warehouse.add_product(product):
                warehouse.add_product(product)
                i += 1

        print(f"{i} products delivered to {warehouse.location} warehouse by {self.name}, "
              f"transaction id: {self.id}, contact details: {self.contact_details}")

    def __str__(self):
        product_list = ", ".join([product.name for product in self.products_supplied])
        return (f"Supplier ID: {self.id}, Name: {self.name}, "
                f"Contact Details: {self.contact_details}, Products Supplied: {product_list}")

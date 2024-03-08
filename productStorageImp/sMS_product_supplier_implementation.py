from productCreationImp.sMS_product_implementation import Product
from productUtilsImp.sMS_Iproduct_handler_implementation import ProductHandler
from productStorageImp.sMS_product_warehouse_implementation import Warehouse
from typing import List


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

    def deliver_supplies(self, warehouse: Warehouse) -> None:
        i = 0

        for product in self.products_supplied:
            if warehouse.add_product(product):
                warehouse.add_product(product)
                i += 1

        print(f"{i} products delivered to {warehouse.location} warehouse by {self.name}, "
              f"transaction id: {self.id}, contact details: {self.contact_details}")

    def __str__(self):
        product_list = ", ".join([product.name for product in self.products_supplied])
        return f"Supplier ID: {self.id}, Name: {self.name}, Contact Details: {self.contact_details}, Products Supplied: {product_list}"
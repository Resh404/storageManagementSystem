from productImp import Product
from typing import List
from warehouseImp import Warehouse


class Supplier:
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

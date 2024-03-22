from typing import List

from productDefinition.product_imp import Product
from productStorage.product_inventory_imp import Inventory
from productStorage.product_supplier_imp import Supplier
from productStorage.product_warehouse_imp import Warehouse

''' Factory class for the classes in the productStorage module'''


class StorageFactory:
    @staticmethod
    def create_product(id: int, name: str, price: float, quantity: int, category: str) -> Product:
        return Product(id, name, price, quantity, category)

    @staticmethod
    def create_inventory() -> Inventory:
        return Inventory()

    @staticmethod
    def create_warehouse(location: str, capacity: int) -> Warehouse:
        return Warehouse(location, capacity)

    @staticmethod
    def create_supplier(id: int, name: str, contact_details: str, products_supplied: List[Product]) -> Supplier:
        return Supplier(id, name, contact_details, products_supplied)

from typing import List
from productCreationImp.sMS_product_implementation import Product
from productStorageImp.sMS_product_inventory_implementation import Inventory
from productStorageImp.sMS_product_warehouse_implementation import Warehouse
from productStorageImp.sMS_product_supplier_implementation import Supplier
from productSaleImp.sMS_order_implementation import Order
from productSaleImp.sMS_customer_implementation import Customer
from productUtilsImp.sMS_product_warehouse_utils_implementation import WarehouseUtils


class Factory:
    @staticmethod
    def create_product(id: int, name: str, price: float, quantity: int, category: str) -> Product:
        return Product(id, name, price, quantity, category)

    @staticmethod
    def create_inventory() -> Inventory:
        return Inventory()

    @staticmethod
    def create_warehouse(location: str, capacity: int, utils: WarehouseUtils) -> Warehouse:
        return Warehouse(location, capacity, utils)

    @staticmethod
    def create_supplier(id: int, name: str, contact_details: str, products_supplied: List[Product]) -> Supplier:
        return Supplier(id, name, contact_details, products_supplied)

    @staticmethod
    def create_order(id: int, products: List[Product]) -> Order:
        return Order(id, products)

    @staticmethod
    def create_customer(id: int, name: str, orders_placed: List[Order]) -> Customer:
        return Customer(id, name, orders_placed)

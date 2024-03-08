from productCreationImp.sMS_product_implementation import Product
from productDatabaseImp.sMS_get_data_from_table_in_database import TableDataFletcher
from productDatabaseImp.sMS_connect_to_database import ConnectToDatabase
from productDatabaseImp.sMS_create_new_storage_database import CreateStorageDatabase
from productStorageImp.sMS_product_inventory_implementation import Inventory
from productStorageImp.sMS_product_warehouse_implementation import Warehouse
from productStorageImp.sMS_product_supplier_implementation import Supplier
from productSaleImp.sMS_order_implementation import Order
from productSaleImp.sMS_customer_implementation import Customer
from typing import List


class Factory:
    @staticmethod
    def create_connection_to_database(host_name: str, user_name: str, password: str, port: int) -> ConnectToDatabase:
        return ConnectToDatabase(host_name, user_name, password, port)

    @staticmethod
    def create_new_storage_database() -> CreateStorageDatabase:
        return CreateStorageDatabase()

    @staticmethod
    def create_database_table_data_getter() -> TableDataFletcher:
        return TableDataFletcher()

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

    @staticmethod
    def create_order(id, product_names: List['str'], product_quantities: List[int], warehouse: Warehouse) -> Order:
        return Order(id, product_names, product_quantities, warehouse)

    @staticmethod
    def create_customer(id: int, name: str, orders_placed: Order) -> Customer:
        return Customer(id, name, orders_placed)

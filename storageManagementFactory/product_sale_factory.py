from typing import List

from productSale.product_customer_imp import Customer
from productSale.product_order_imp import Order
from productStorage.product_warehouse_imp import Warehouse

''' Factory class for the classes in the productSale module'''


class SaleFactory:
    @staticmethod
    def create_order(id, product_names: List[str], product_quantities: List[int], warehouse: Warehouse) -> Order:
        return Order(id, product_names, product_quantities, warehouse)

    @staticmethod
    def create_customer(id: int, name: str, email: str, orders_placed: Order) -> Customer:
        return Customer(id, name, email, orders_placed)

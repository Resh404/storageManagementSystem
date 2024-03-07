from productUtilsImp.sMS_Iorder_handler_implementation import OrderHandler
from productSaleImp.sMS_order_implementation import Order
from typing import List


class Customer(OrderHandler):
    def __init__(self, id: int, name: str, orders_placed: List['Order']):
        self.id = id
        self.name = name
        self.orders_placed = orders_placed

    def calculate_total_cost(self, my_orders: List[Order]) -> float:
        total_cost = 0
        for order in my_orders:
            for product in order.products:
                total_cost += product.price * product.quantity
        return total_cost

    def place_order(self, order: Order) -> None:
        self.orders_placed.append(order)

    def cancel_order(self, order: Order) -> None:
        self.orders_placed.remove(order)

    def print_orders_placed(self):
        for order in self.orders_placed:
            print(str(order))

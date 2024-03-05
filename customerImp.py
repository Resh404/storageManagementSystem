from typing import List
from orderImp import Order


class Customer:
    def __init__(self, id: int, name: str, contact_details: str, orders_placed: List['Order']) -> None:
        self.id = id
        self.name = name
        self.contact_details = contact_details
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

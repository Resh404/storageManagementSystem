from productUtilsImp.sMS_Iorder_handler_implementation import OrderHandler
from productSaleImp.sMS_order_implementation import Order


class Customer(OrderHandler):
    def __init__(self, id: int, name: str, orders_placed: Order):
        self.id = id
        self.name = name
        self.orders_placed = orders_placed
        self.orders_being_processed = []

    def calculate_total_cost(self) -> float:
        total_cost = 0
        for product in self.orders_placed.products:
            total_cost += product.price * product.quantity
        return total_cost

    def place_order(self) -> None:
        self.orders_placed.reserve_product_from_warehouse()
        self.orders_being_processed.append(self.orders_placed)

    def cancel_order(self, order: Order) -> None:
        self.orders_being_processed.remove(order)

    def print_orders_placed(self):
        total_cost = 0
        for order in self.orders_being_processed:
            for product in order.reserved_products_list:
                print(f"{product.name}, Quantity: {product.quantity}, Price/ea: {product.price}")
                total_cost += product.price * product.quantity
        print(f"Total cost: ${total_cost:.2f}")

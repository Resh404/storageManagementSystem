from productUtils.Iorder_handler_imp import OrderHandler
from productSale.product_order_imp import Order

''' This class defines a customer and what customer can do.
The class implements the OrderHandler interface which defines the bare minimum methods it need.
The initialized parameters defines what a customer need to be initialized with.
The names of the methods explains the functionality of the method. '''


class Customer(OrderHandler):
    def __init__(self, id: int, name: str, email: str, orders_placed: Order):
        self.id = id
        self.name = name
        self.email = email
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

    def print_products_in_orders(self):
        total_cost = 0
        for product in self.orders_placed.products:
            print(f"{product.name}, Quantity: {product.quantity}, Price/ea: {product.price}")
            total_cost += product.price * product.quantity
        print(f"Total cost: ${total_cost:.2f}")

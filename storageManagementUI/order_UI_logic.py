from productDatabaseQueries.insert_product_query_handler import InsertProductHandler
from productSale.product_customer_imp import Customer
from productSale.product_order_imp import Order

''' This class contains the logic that allows the user manipulate with products in their order/basket. 
The names of the methods explains the functionality of the method. '''


class OrderChoices:
    @staticmethod
    def add_product(customer_order: Order):
        print("'quit' to cancel")

        while True:
            print("Name of product to be added: ")
            product_to_add_name = input().lower()
            if not product_to_add_name or product_to_add_name == "quit":
                if product_to_add_name == "quit":
                    return
                print("Invalid input")
                continue

            print("Product quantity: ")
            product_to_add_quantity = input()
            if not product_to_add_quantity:
                print("Quantity cannot be empty")
                continue

            try:
                product_to_add_quantity = int(product_to_add_quantity)
            except ValueError:
                print("Quantity must be an integer")
                continue

            if product_to_add_quantity <= 0:
                print("Quantity must be greater than 0")
                continue

            customer_order.add_product(product_to_add_name, product_to_add_quantity)

    @staticmethod
    def remove_product(customer_order: Order):
        print("'quit' to cancel")

        while True:
            print("Name of product to be removed: ")
            product_to_add_name = input().lower()
            if not product_to_add_name or product_to_add_name == "quit":
                if product_to_add_name == "quit":
                    return
                print("Invalid input")
                continue

            customer_order.remove_product(product_to_add_name)

    @staticmethod
    def show_customer_products(customer: Customer):
        customer.print_products_in_orders()

    @staticmethod
    def confirm_order(customer: Customer, customer_order: Order):
        if not customer_order.products:
            print("No products chosen")
            return
        print("These are your products: ")
        OrderChoices.show_customer_products(customer)

        print("Would you like to proceed to payment and delivery options y/n?")
        proceed_to_checkout = input().lower()

        if proceed_to_checkout == "yes" or proceed_to_checkout == "y":
            customer.place_order()
            for product in customer_order.products:
                InsertProductHandler.insert_product_in_transaction_history_table(product.id,
                                                                                 customer.id, product.quantity,
                                                                                 "purchase")
            print("Successfully placed order. Thank you for your purchase")

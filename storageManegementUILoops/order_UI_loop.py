import sys

from productSale.product_customer_imp import Customer
from productSale.product_order_imp import Order
from storageManagementUI.order_UI_logic import OrderChoices

''' This class contains the order/basket options a customer is presented with when the system is running.'''


class OrderUILoop:
    @staticmethod
    def order_options(customer: Customer):
        while True:
            print("\n1. Add a product to basket\n"
                  "2. Remove a product from basket\n"
                  "3. Show products in basket\n"
                  "4. Confirm order\n"
                  "5. Exit")
            order_choice = input("Enter your choice:\n ")

            if order_choice == '1':
                OrderChoices.add_product(customer)
            elif order_choice == '2':
                OrderChoices.remove_product(customer)
            elif order_choice == '3':
                OrderChoices.show_customer_products(customer)
            elif order_choice == '4':
                OrderChoices.confirm_order(customer)
                return True
            elif order_choice == '5':
                sys.exit()
            else:
                print("Invalid input")
                continue

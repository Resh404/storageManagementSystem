import sys

from storageManagementUI.customer_UI_logic import CustomerChoices

''' This class contains the options a customer is presented with when the system is running.'''


class CustomerUILoop:
    @staticmethod
    def customer_options():
        while True:
            print("If you are an existing customer please login else please register")
            print("1: Login\n"
                  "2: Registration\n"
                  "3: Exit")
            customer_specification = input("Enter your choice: ")

            if customer_specification == '1':
                login_mail = CustomerChoices.customer_login()
                return login_mail
            elif customer_specification == '2':
                registration_mail = CustomerChoices.customer_registration()
                return registration_mail
            elif customer_specification == '3':
                print("Thank you for visiting. Goodbye!")
                sys.exit()
            else:
                print("Invalid input, please try again")
                continue

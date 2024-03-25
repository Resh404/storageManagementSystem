from customerDatabaseQueries.insert_customer_query_handler import InsertCustomerHandler
from storageManagementUIUtils.UI_utils import UtilsForUI

''' This class contains the logic that allows the user register or login the storage management system.
Instead of having everything in main the terminal interaction have been split up into separate parts, 
were this part controls the user registration and login behaviour of the system. 
The names of the methods explains the functionality of the method. '''


class CustomerChoices:
    @staticmethod
    def customer_registration() -> str:
        while True:
            print("Enter a username you would like: ")
            username = input().strip().lower()

            if not username:
                print("Username cannot be empty")
                continue

            print("Enter email: ")
            email = input().strip().lower()

            if not email:
                print("Email cannot be empty")
                continue

            if UtilsForUI.check_if_customer_exists(email):
                print("Email already registered")
                return email

            # Insert the customer into the database
            if InsertCustomerHandler.insert_customer_in_customers_table(username, email, 0):
                print("Registered successfully")
                return email
            else:
                print("Registration failed. Please try again.")

    @staticmethod
    def customer_login() -> str:
        while True:
            print("Enter email: ")
            email = input().strip().lower()

            if not email:
                print("Email cannot be empty")
                continue

            email_check = UtilsForUI.check_if_customer_exists(email)

            if email_check is not None:
                print(f"Welcome {email_check[1]}")
                return email
            else:
                print("Login failed. Email not found")
                return None

import mysql.connector

from customerDatabaseQueries.customer_queries import DatabaseCustomerQueries
from storageManagementDatabase.connect_to_database import ConnectToDatabase

''' This classes methods uses the update queries from the customer_queries file.
the main purpose of this class is to update existing customers information in the customer table in the database.
The name of the methods entails what the method does. '''


class UpdateCustomerHandler:
    @staticmethod
    def update_customer_name(customer_id: int, new_name: str) -> bool:
        try:
            query = DatabaseCustomerQueries.customer_name_updater_by_id(new_name, customer_id)
            my_database = ConnectToDatabase.connect_to_database()
            cursor = my_database.cursor()
            cursor.execute(query, (new_name, customer_id,))

            my_database.commit()
            cursor.close()

            return True
        except mysql.connector.Error as e:
            print(f"MySQL error update customer name: {e}")
            return False

    @staticmethod
    def update_customer_email(customer_id: int, new_email: str) -> bool:
        try:
            query = DatabaseCustomerQueries.customer_email_updater_by_id(new_email, customer_id)
            my_database = ConnectToDatabase.connect_to_database()
            cursor = my_database.cursor()
            cursor.execute(query, (new_email, customer_id,))

            my_database.commit()
            cursor.close()

            return True
        except mysql.connector.Error as e:
            print(f"MySQL error update customer email: {e}")
            return False

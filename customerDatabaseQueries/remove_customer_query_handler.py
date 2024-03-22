import mysql.connector

from customerDatabaseQueries.customer_queries import DatabaseCustomerQueries
from storageManagementDatabase.connect_to_database import ConnectToDatabase

''' This classes methods uses the delete queries from the customer_queries file.
the main purpose of this class is to remove a existing customer from the customer table in the database.
The name of the methods entails what the method does. '''


class RemoveCustomerHandler:
    @staticmethod
    def remove_customer_by_id(customer_id: int) -> bool:
        try:
            query = DatabaseCustomerQueries.customer_remover_by_id(customer_id)
            my_database = ConnectToDatabase.connect_to_database()
            cursor = my_database.cursor()
            cursor.execute(query, (customer_id,))

            my_database.commit()
            cursor.close()

            return True
        except mysql.connector.Error as e:
            print(f"MySQL error remove customer id: {e}")
            return False

    @staticmethod
    def remove_customer_by_name(customer_name: str) -> bool:
        try:
            query = DatabaseCustomerQueries.customer_remover_by_name(customer_name)
            my_database = ConnectToDatabase.connect_to_database()
            cursor = my_database.cursor()
            cursor.execute(query, (customer_name,))

            my_database.commit()
            cursor.close()

            return True
        except mysql.connector.Error as e:
            print(f"MySQL error remove customer name: {e}")
            return False

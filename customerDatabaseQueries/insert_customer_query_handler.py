from datetime import datetime

import mysql.connector

from customerDatabaseQueries.customer_queries import DatabaseCustomerQueries
from storageManagementDatabase.connect_to_database import ConnectToDatabase

''' This classes methods uses the insert queries from the customer_queries file.
the main purpose of this class is to insert customer new customers into the customer table in the database.
The name of the methods entails what the method does. '''


class InsertCustomerHandler:
    @staticmethod
    def insert_customer_in_customers_table(name: str, email: str, total_orders: int) -> bool:
        try:
            today = datetime.now()
            query = DatabaseCustomerQueries.insert_customer(name, email, total_orders, today)
            my_database = ConnectToDatabase.connect_to_database()
            cursor = my_database.cursor()
            cursor.execute(query, (name, email, total_orders, today))

            my_database.commit()
            cursor.close()

            return True
        except mysql.connector.Error as e:
            print(f"MySQL error insert customer: {e}")
            return False

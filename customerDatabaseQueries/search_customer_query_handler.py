from datetime import datetime

import mysql.connector

from customerDatabaseQueries.customer_queries import DatabaseCustomerQueries
from storageManagementDatabase.connect_to_database import ConnectToDatabase

''' This classes methods uses the retrieve queries from the customer_queries file.
the main purpose of this class is to search for existing customers from the customer table in the database.
The name of the methods entails what the method does. '''


class SearchCustomerHandler:
    @staticmethod
    def search_customer_by_id(customer_id: int):
        try:
            query = DatabaseCustomerQueries.customer_getter_by_id(customer_id)
            my_database = ConnectToDatabase.connect_to_database()
            cursor = my_database.cursor()
            cursor.execute(query, (customer_id,))

            result = cursor.fetchone()
            cursor.close()

            return result
        except mysql.connector.Error as e:
            print(f"MySQL error search customer id: {e}")
            return None

    @staticmethod
    def search_customer_by_name(customer_name: str):
        try:
            query = DatabaseCustomerQueries.customer_getter_by_name(customer_name)
            my_database = ConnectToDatabase.connect_to_database()
            cursor = my_database.cursor()
            cursor.execute(query, (customer_name,))

            result = cursor.fetchall()
            cursor.close()

            return result
        except mysql.connector.Error as e:
            print(f"MySQL error search customer name: {e}")
            return None

    @staticmethod
    def search_customer_by_email(email: str):
        try:
            query = DatabaseCustomerQueries.customer_getter_by_email(email)
            my_database = ConnectToDatabase.connect_to_database()
            cursor = my_database.cursor()
            cursor.execute(query, (email,))

            result = cursor.fetchall()
            cursor.close()

            return result
        except mysql.connector.Error as e:
            print(f"MySQL error search customer mail: {e}")
            return None

    @staticmethod
    def search_customer_by_order_size(min_orders: int, max_orders: int):
        try:
            query = DatabaseCustomerQueries.customer_getter_by_order_size(min_orders, max_orders)
            my_database = ConnectToDatabase.connect_to_database()
            cursor = my_database.cursor()
            cursor.execute(query, (min_orders, max_orders,))

            result = cursor.fetchall()
            cursor.close()

            return result
        except mysql.connector.Error as e:
            print(f"MySQL error search customer order size: {e}")
            return None

    @staticmethod
    def search_customer_by_date(date1: datetime, date2: datetime):
        try:
            query = DatabaseCustomerQueries.customer_getter_by_date(date1, date2)
            my_database = ConnectToDatabase.connect_to_database()
            cursor = my_database.cursor()
            cursor.execute(query, (date1, date2))

            result = cursor.fetchall()
            cursor.close()

            return result
        except mysql.connector.Error as e:
            print(f"MySQL error search customer date: {e}")
            return None

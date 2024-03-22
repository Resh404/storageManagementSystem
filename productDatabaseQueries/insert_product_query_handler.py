from datetime import datetime

import mysql.connector

from storageManagementDatabase.connect_to_database import ConnectToDatabase
from productDatabaseQueries.product_queries import DatabaseProductQueries

''' This classes methods uses the insert queries from the product_queries file.
the main purpose of this class is to insert customer new products into the products table in the database.
The name of the methods entails what the method does. '''


class InsertProductHandler:
    @staticmethod
    def insert_product_in_products_table(name: str, price: float, quantity: int, category: str) -> bool:
        try:
            query = DatabaseProductQueries.insert_product_products(name, price, quantity, category)
            my_database = ConnectToDatabase.connect_to_database()
            cursor = my_database.cursor()
            cursor.execute(query, (name, price, quantity, category,))

            my_database.commit()
            cursor.close()

            return True
        except mysql.connector.Error as e:
            print(f"MySQL error insert product into products table: {e}")
            return False

    @staticmethod
    def insert_product_in_transaction_history_table(product_id: int, customer_id: int,
                                                    product_quantity: int, transaction_type: str) -> bool:
        today = datetime.now()
        try:
            query = DatabaseProductQueries.insert_product_in_history(product_id, customer_id,
                                                                     product_quantity, transaction_type, today)
            my_database = ConnectToDatabase.connect_to_database()
            cursor = my_database.cursor()
            cursor.execute(query, (product_id, customer_id, product_quantity, transaction_type, today,))

            my_database.commit()
            cursor.close()
        except mysql.connector.Error as e:
            print(f"MySQL error insert product into the transaction history table: {e}")

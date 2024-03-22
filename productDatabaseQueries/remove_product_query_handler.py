import mysql.connector

from storageManagementDatabase.connect_to_database import ConnectToDatabase
from productDatabaseQueries.product_queries import DatabaseProductQueries

''' This classes methods uses the remove queries from the product_queries file.
the main purpose of this class is to remove existing products from the products table in the database.
The name of the methods entails what the method does. '''


class RemoveProductHandler:
    @staticmethod
    def remove_product_by_id(product_id: int) -> bool:
        try:
            query = DatabaseProductQueries.product_remover_by_id(product_id)
            my_database = ConnectToDatabase.connect_to_database()
            cursor = my_database.cursor()
            cursor.execute(query, (product_id,))

            my_database.commit()
            cursor.close()

            return True
        except mysql.connector.Error as e:
            print(f"MySQL error remove product id: {e}")
            return False

    @staticmethod
    def remove_product_by_name(product_name: str) -> bool:
        try:
            query = DatabaseProductQueries.product_remover_by_name(product_name)
            my_database = ConnectToDatabase.connect_to_database()
            cursor = my_database.cursor()
            cursor.execute(query, (product_name,))

            my_database.commit()
            cursor.close()

            return True
        except mysql.connector.Error as e:
            print(f"MySQL error remove product name: {e}")
            return False

    @staticmethod
    def remove_product_by_category(product_category: str) -> bool:
        try:
            query = DatabaseProductQueries.product_remover_by_category(product_category)
            my_database = ConnectToDatabase.connect_to_database()
            cursor = my_database.cursor()
            cursor.execute(query, (product_category,))

            my_database.commit()
            cursor.close()

            return True
        except mysql.connector.Error as e:
            print(f"MySQL error remove product category: {e}")
            return False

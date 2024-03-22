import mysql.connector

from storageManagementDatabase.connect_to_database import ConnectToDatabase
from productDatabaseQueries.product_queries import DatabaseProductQueries

''' This classes methods uses the update queries from the product_queries file.
the main purpose of this class is to update existing products in the products table in the database.
The name of the methods entails what the method does. '''


class UpdateProductHandler:
    @staticmethod
    def update_product_name(product_id: int, product_name: str) -> bool:
        try:
            query = DatabaseProductQueries.product_name_updater_by_id(product_name, product_id)
            my_database = ConnectToDatabase.connect_to_database()
            cursor = my_database.cursor()
            cursor.execute(query, (product_name, product_id,))

            my_database.commit()
            cursor.close()

            return True
        except mysql.connector.Error as e:
            print(f"MySQL error update product name: {e}")
            return False

    @staticmethod
    def update_product_price(product_id: int, product_price: float) -> bool:
        try:
            query = DatabaseProductQueries.product_price_updater_by_id(product_price, product_id)
            my_database = ConnectToDatabase.connect_to_database()
            cursor = my_database.cursor()
            cursor.execute(query, (product_price, product_id,))

            my_database.commit()
            cursor.close()

            return True
        except mysql.connector.Error as e:
            print(f"MySQL error update product price: {e}")
            return False

    @staticmethod
    def update_product_quantity(product_id: int, product_quantity: int) -> bool:
        try:
            query = DatabaseProductQueries.product_quantity_updater_by_id(product_quantity, product_id)
            my_database = ConnectToDatabase.connect_to_database()
            cursor = my_database.cursor()
            cursor.execute(query, (product_quantity, product_id,))

            my_database.commit()
            cursor.close()

            return True
        except mysql.connector.Error as e:
            print(f"MySQL error update product quantity: {e}")
            return False

    @staticmethod
    def update_product_category(product_id: int, product_category: str) -> bool:
        try:
            query = DatabaseProductQueries.product_category_updater_by_id(product_category, product_id)
            my_database = ConnectToDatabase.connect_to_database()
            cursor = my_database.cursor()
            cursor.execute(query, (product_category, product_id,))

            my_database.commit()
            cursor.close()

            return True
        except mysql.connector.Error as e:
            print(f"MySQL error update product category: {e}")
            return False
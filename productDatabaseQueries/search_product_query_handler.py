from typing import List
import mysql.connector

from storageManagementDatabase.connect_to_database import ConnectToDatabase
from productDefinition.product_imp import Product
from productDatabaseQueries.product_queries import DatabaseProductQueries

''' This classes methods uses the search queries from the product_queries file.
the main purpose of this class is to search for existing products in the products table in the database.
The name of the methods entails what the method does. '''


class SearchProductHandler:
    @staticmethod
    def search_product_by_id(product_id: int) -> Product:
        try:
            query = DatabaseProductQueries.product_getter_by_id(product_id)
            my_database = ConnectToDatabase.connect_to_database()
            cursor = my_database.cursor()
            cursor.execute(query, (product_id,))

            result = cursor.fetchone()
            cursor.close()

            return Product(*result) if result else None
        except mysql.connector.Error as e:
            print(f"MySQL error search product id: {e}")
            return None

    @staticmethod
    def search_product_by_name(product_name: str) -> Product:
        try:
            query = DatabaseProductQueries.product_getter_by_name(product_name)
            my_database = ConnectToDatabase.connect_to_database()
            cursor = my_database.cursor()
            cursor.execute(query, (product_name,))

            result = cursor.fetchall()
            cursor.close()

            return Product(*result) if result else None
        except mysql.connector.Error as e:
            print(f"MySQL error search product name: {e}")
            return None

    @staticmethod
    def search_product_by_category(product_category: str) -> List['Product']:
        try:
            query = DatabaseProductQueries.product_getter_by_category(product_category)
            my_database = ConnectToDatabase.connect_to_database()
            cursor = my_database.cursor()
            cursor.execute(query, (product_category,))

            results = cursor.fetchall()
            cursor.close()

            products = []
            for result in results:
                products.append(Product(*result))

            return products
        except mysql.connector.Error as e:
            print(f"MySQL error search product category: {e}")
            return []

from storageManagementDatabase.connect_to_database import ConnectToDatabase
from typing import List, Tuple
import mysql.connector

''' This class creates the products table in the database and uploads the data 
from the file data_for_database to the database.
The names of the methods explains the functionality of the method. '''


class CreateStorageDatabase:
    @staticmethod
    def create_products_table_with_data(database_name: str, product_data: List[Tuple]) -> None:
        try:
            # Connect to the server
            my_database = ConnectToDatabase.connect_to_database(database_name)
            my_database.database = database_name

            cursor = my_database.cursor()

            # Switch to the specified database
            cursor.execute(f"USE {database_name}")

            # Create the product table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS products (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255),
                    price FLOAT,
                    quantity INT,
                    category VARCHAR(255)
                )
            """)

            # Insert product data into the table
            insert_query = "INSERT INTO products (name, price, quantity, category) VALUES (%s, %s, %s, %s)"
            cursor.executemany(insert_query, product_data)

            my_database.commit()
            cursor.close()
            my_database.close()

            print(f"Products data added to '{database_name}' successfully.")
        except mysql.connector.Error as e:
            print(f"Error creating storage database: {e}")

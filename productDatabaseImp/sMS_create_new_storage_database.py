from productDatabaseImp.sMS_connect_to_database import ConnectToDatabase
from typing import List, Tuple
import mysql.connector


class CreateStorageDatabase:
    def create_database(self, database_name: str, product_data: List[Tuple], server_connector: ConnectToDatabase) -> None:
        try:
            # Connect to the server
            my_database = server_connector.connect_to_database(database_name)
            my_database.database = database_name

            # Create a cursor object
            cursor = my_database.cursor()

            # Create the database if it doesn't exist
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")

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

            # Commit changes and close cursor and connection
            my_database.commit()

            # Insert product data into the table
            insert_query = "INSERT INTO products (name, price, quantity, category) VALUES (%s, %s, %s, %s)"
            cursor.executemany(insert_query, product_data)

            my_database.commit()
            cursor.close()
            my_database.close()

            print(f"Storage database '{database_name}' created successfully.")
        except mysql.connector.Error as e:
            print(f"Error creating storage database: {e}")


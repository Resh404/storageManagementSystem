import mysql.connector

from storageManagementDatabase.connect_to_database import ConnectToDatabase
from storageManagementDatabase.create_new_storage_database import CreateStorageDatabase
from storageManagementDatabase.data_for_database import product_data

''' This script sets up the database with the right name, tables, tables values, and data for table products '''


def database_setup():
    try:
        my_database = ConnectToDatabase.connect_to_database("storage_database")
        CreateStorageDatabase.create_products_table_with_data("storage_database", product_data)

        cursor = my_database.cursor()

        # Create tables
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                email VARCHAR(255),
                total_orders INT,
                registration_date DATETIME
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS transaction_history (
                id INT AUTO_INCREMENT PRIMARY KEY,
                product_id INT,
                customer_id INT,
                product_quantity INT, 
                transaction_type VARCHAR(255),
                time_of_transaction DATETIME,
                FOREIGN KEY (product_id) REFERENCES products(id),
                FOREIGN KEY (customer_id) REFERENCES customers(id))
        """)

        my_database.commit()
        cursor.close()
        my_database.close()

    except mysql.connector.Error as e:
        print(f"MySQL error: {e}")

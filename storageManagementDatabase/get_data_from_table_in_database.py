from storageManagementDatabase.connect_to_database import ConnectToDatabase
from productDefinition.product_imp import Product
from typing import List
import mysql.connector

''' This class yields rows in batches from the specified table in the database. '''


class TableDataFletcher:
    @staticmethod
    def get_table_data(table_name: str) -> List['Product']:
        try:
            # Connect to the database
            my_database = ConnectToDatabase.connect_to_database()
            cursor = my_database.cursor()

            # Select all data from the specified table
            cursor.execute(f"SELECT * FROM {table_name}")

            # Fetch data in batches
            while True:
                rows = cursor.fetchmany(5)
                if not rows:
                    break
                yield rows

            cursor.close()
            my_database.close()
        except mysql.connector.Error as e:
            print(f"Error fetching data from table: {e}")
            return None

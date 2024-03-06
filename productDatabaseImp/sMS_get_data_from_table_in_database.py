from productCreationImp.sMS_product_implementation import Product
from typing import List
import mysql.connector


class TableDataFletcher:
    def get_table_data(self, table_name: str, database_connector: mysql.connector.connection.MySQLConnection) -> List['Product']:
        try:
            # Connect to the database
            my_database = database_connector
            cursor = my_database.cursor()

            # Select all data from the specified table
            cursor.execute(f"SELECT * FROM {table_name}")

            # Fetch data in batches
            while True:
                rows = cursor.fetchmany(100)
                if not rows:
                    break
                yield rows
        except mysql.connector.Error as e:
            print(f"Error fetching data from table: {e}")
            return None
        finally:
            # Close cursor and database connection
            cursor.close()
            my_database.close()
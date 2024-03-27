from productUtils.singleton_imp import Singleton
import mysql.connector
import json


''' This class manages the manages the connection to the database.
The class inherits from the Singleton to ensure that is only one connection at all times.
The initialized parameters in _connect_to_server defines the necessary information in order 
to establish connection to the database.
The names of the static methods explains the functionality of the method. '''


class ConnectToDatabase(Singleton):
    @staticmethod
    def _connect_to_server() -> mysql.connector:
        try:
            # Read database configuration from JSON file
            with open('config.json') as f:
                config = json.load(f)
                database_config = config.get('database', {})

            # Connect to the server
            my_database = mysql.connector.connect(**database_config)

            return my_database
        except mysql.connector.Error as e:
            print(f"Error connecting to the database: {e}")
            raise

    @staticmethod
    def connect_to_database(database_name="storage_database") -> mysql.connector.connection.MySQLConnection:
        try:
            # Connect to the specified server
            my_database = ConnectToDatabase._connect_to_server()

            # Check if the database exists
            cursor = my_database.cursor()
            cursor.execute(f"SHOW DATABASES LIKE '{database_name}'")
            existing_databases = cursor.fetchall()
            cursor.close()

            if not existing_databases:
                # Create the database if it does not exist
                cursor = my_database.cursor()
                cursor.execute(f"CREATE DATABASE {database_name}")
                cursor.close()
                print(f"Database '{database_name}' created successfully.")

            # Specify the database name
            my_database.database = database_name

            return my_database
        except mysql.connector.Error as e:
            print(f"Error connecting to the database: {e}")
            raise

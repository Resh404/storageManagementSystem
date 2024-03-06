from productUtilsImp.sMS_singleton_implementation import Singleton
import mysql.connector


class ConnectToDatabase(Singleton):
    # define database variables
    def __init__(self, host_name: str, user_name: str, password: str, port: int):
        self.host_name = host_name
        self.user_name = user_name
        self.password = password
        self.port = port

    def _connect_to_server(self) -> mysql.connector:
        try:
            # Connect to the server
            my_database = mysql.connector.connect(
                host=self.host_name,
                user=self.user_name,
                password=self.password,
                port=self.port
            )
            return my_database
        except mysql.connector.Error as e:
            print(f"Error connecting to the database: {e}")
            raise

    def connect_to_database(self, database_name: str) -> mysql.connector.connection.MySQLConnection:
        try:
            # Connect to the specified server
            my_database = self._connect_to_server()

            # Specify the database name
            my_database.database = database_name

            # Check if the database exists
            cursor = my_database.cursor()
            cursor.execute(f"SHOW DATABASES LIKE '{database_name}'")
            existing_databases = cursor.fetchall()
            cursor.close()

            if not existing_databases:
                raise Exception(f"Database '{database_name}' does not exist")

            return my_database
        except Exception as e:
            print(f"Error connecting to the database: {e}")
            raise

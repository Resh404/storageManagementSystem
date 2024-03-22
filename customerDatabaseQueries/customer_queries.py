from datetime import datetime

''' This class have the queries which will be used to interact with the customers table
in the database. 
There are queries for retrieving customer information from the database, updating existing 
customer information in the database, deleting customer from the database, and inserting new customer 
into the database. '''


class DatabaseCustomerQueries:
    # Get customer information from database
    @staticmethod
    def customer_getter_by_id(id: int) -> str:
        sql_query = "SELECT * FROM customers WHERE id = %s"
        return sql_query

    @staticmethod
    def customer_getter_by_name(name: str) -> str:
        sql_query = "SELECT * FROM customers WHERE name = %s"
        return sql_query

    @staticmethod
    def customer_getter_by_email(email: str) -> str:
        sql_query = "SELECT * FROM customers WHERE email = %s"
        return sql_query

    @staticmethod
    def customer_getter_by_order_size(min_orders: int, max_orders: int) -> str:
        sql_query = "SELECT * FROM customers WHERE total_orders BETWEEN %s AND %s"
        return sql_query

    @staticmethod
    def customer_getter_by_date(from_date: datetime, to_date: datetime) -> str:
        sql_query = "SELECT * FROM customers WHERE registration_date BETWEEN %s AND %s"
        return sql_query

    # Update customer information in database
    @staticmethod
    def customer_name_updater_by_id(new_name: str, customer_id: int) -> str:
        sql_query = "UPDATE customers SET name = %s WHERE id = %s"
        return sql_query

    @staticmethod
    def customer_email_updater_by_id(new_email: str, customer_id: int) -> str:
        sql_query = "UPDATE customers SET email = %s WHERE id = %s"
        return sql_query

    # Remove customer from database
    @staticmethod
    def customer_remover_by_id(id: int) -> str:
        sql_query = "DELETE FROM customers WHERE id = %s"
        return sql_query

    @staticmethod
    def customer_remover_by_name(name: str) -> str:
        sql_query = "DELETE FROM customers WHERE name = %s"
        return sql_query

    # Insert customer to database
    @staticmethod
    def insert_customer(name: str, email: str, total_orders: int, registration_date: datetime) -> str:
        sql_query = "INSERT INTO customers (name, email, total_orders, registration_date) VALUES (%s, %s, %s, %s)"
        return sql_query

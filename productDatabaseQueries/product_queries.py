

''' This class have the queries which will be used to interact with the products table
in the database.
There are queries for retrieving products information from the database, updating existing
products information in the database, deleting products from the database, and inserting new products
into the database. '''


class DatabaseProductQueries:
    # Get product information from database
    @staticmethod
    def product_getter_by_id(id: int) -> str:
        sql_query = "SELECT * FROM products WHERE id = %s"
        return sql_query

    @staticmethod
    def product_getter_by_name(name: str) -> str:
        sql_query = "SELECT * FROM products WHERE name = %s"
        return sql_query

    @staticmethod
    def product_getter_by_category(category: str) -> str:
        sql_query = "SELECT * FROM products WHERE category = %s"
        return sql_query

    # Update product information in database
    @staticmethod
    def product_name_updater_by_id(new_name: str, product_id: int) -> str:
        sql_query = "UPDATE products SET name = %s WHERE id = %s"
        return sql_query

    @staticmethod
    def product_price_updater_by_id(new_price: float, product_id: int) -> str:
        sql_query = "UPDATE products SET price = %s WHERE id = %s"
        return sql_query

    @staticmethod
    def product_quantity_updater_by_id(new_quantity: int, product_id: int) -> str:
        sql_query = "UPDATE products SET quantity = %s WHERE id = %s"
        return sql_query

    @staticmethod
    def product_category_updater_by_id(new_category: str, product_id: int) -> str:
        sql_query = "UPDATE products SET category = %s WHERE id = %s"
        return sql_query

    # remove product from database
    @staticmethod
    def product_remover_by_id(id: int) -> str:
        sql_query = "DELETE FROM products WHERE id = %s"
        return sql_query

    @staticmethod
    def product_remover_by_name(name: str) -> str:
        sql_query = "DELETE FROM products WHERE name = %s"
        return sql_query

    @staticmethod
    def product_remover_by_category(category: str) -> str:
        sql_query = "DELETE FROM products WHERE category = %s"
        return sql_query

    # Insert product to database
    @staticmethod
    def insert_product_products(name: str, price: float, quantity: int, category: str) -> str:
        sql_query = "INSERT INTO products (name, price, quantity, category) VALUES (%s, %s, %s, %s)"
        return sql_query

    @staticmethod
    def insert_product_in_history(product_id: int, customer_id: int, product_quantity: int,
                                  transaction_type, time_of_transaction) -> str:
        sql_query = ("INSERT INTO transaction_history (product_id, customer_id, product_quantity, "
                     "transaction_type, time_of_transaction) VALUES (%s, %s, %s, %s, %s)")
        return sql_query

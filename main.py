from productUtilsImp.sMS_product_factory_implementation import Factory
from productDatabaseImp.sMS_data_for_database import product_data
import mysql.connector


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    my_server_connection = Factory.create_connection_to_database("localhost", "root", "Kom12345", 3306)
    my_created_database = Factory.create_new_storage_database()
    my_data_fletcher = Factory.create_database_table_data_getter()
    my_inventory = Factory.create_inventory()
    my_warehouse = Factory.create_warehouse("Aarhus", 2000)
    # my_supplier =
    # my_orders =
    # my_customer =

    # my_created_database.create_database("storage_database", product_data, my_server_connection)
    my_database = my_server_connection.connect_to_database("storage_database")

    # Use the data fletched from the database to create instanced of products
    # that are added to the warehouse
    for batch in my_data_fletcher.get_table_data("products", my_database):
        for product_tuple in batch:
            product = Factory.create_product(*product_tuple)

            print(str(product))
            my_warehouse.add_product(product)




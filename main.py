from productDatabaseImp.sMS_ConnectToExistingDatabase import ConnectToDatabase
from productStorageImp.sMS_product_inventory_implementation import Inventory
from productCreationImp.sMS_product_implementation import Product

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    my_database = ConnectToDatabase("localhost", "root", "Kom12345", 3306)
    product1 = Product(1, "apple", 10, 2, "fruit")
    inven = Inventory()

    inven.add_product(product1)
    print(inven.get_product_details(1))
    inven.update_product_details(product_id=1, new_quantity=10)

    # employee_database = my_database.database_connection("employees")
    # employee_salaries_table = my_database.get_table_data("salaries", employee_database)

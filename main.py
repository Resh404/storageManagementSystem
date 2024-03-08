from productUtilsImp.sMS_product_factory_implementation import Factory
import os
import sys

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    my_server_connection = Factory.create_connection_to_database("localhost", "root",
                                                                 "Kom12345", 3306)
    my_created_database = Factory.create_new_storage_database()
    my_data_fletcher = Factory.create_database_table_data_getter()
    my_inventory = Factory.create_inventory()
    my_warehouse = Factory.create_warehouse("Aarhus", 5000)
    # my_supplier =
    # my_orders =
    # my_customer =

    # my_created_database.create_database("storage_database", product_data, my_server_connection)
    my_database = my_server_connection.connect_to_database("storage_database")

    available_categories = ["food", "drink", "electronics"]
    while True:
        category = input(f"What category of product are you looking for? the choices are: "
                         f"{', '.join(available_categories)}: ").lower()
        if category not in available_categories:
            print("Invalid category choice. Please choose from the given categories.")
            continue
        # Use the data fletched from the database to create instanced of products
        # that are added to the warehouse
        for batch in my_data_fletcher.get_table_data("products", my_database):
            for product_tuple in batch:
                product = Factory.create_product(*product_tuple)

                if product.category.lower() == category:
                    sys.stdout = open(os.devnull, 'w')
                    my_warehouse.add_product(product)
                    sys.stdout = sys.__stdout__
                    print(f"Product available: {product.name}, quantity: {product.quantity}")
        break

    customers_processed = 0

    while True:
        add_order = input("Would you like to add an order? (y/n): ").lower()
        if add_order in ["n", "no"]:
            sys.exit()

        customers_processed += 1

        # Create order (basket) so customer can shop from warehouse
        product_names = []
        quantities = []
        customer_order = Factory.create_order(customers_processed, product_names, quantities, my_warehouse)

        while True:
            product_name = input("Enter the product name: ")
            quantity = int(input("Enter the quantity: "))
            customer_order.add_product(product_name, quantity)

            more_products = input("Do you want to order more products? (y/n): ").lower()
            if more_products in ["n", "no"]:
                break

        # Get customer details
        print("Please enter customer details:")
        customer_id = customers_processed
        customer_name = input("Enter customer name: ")

        # Create customer object and associate with orders
        my_customer = Factory.create_customer(customer_id, customer_name, customer_order)
        my_customer.place_order()

        # Display customer's orders
        print(f"Customer {my_customer.name}'s order consists of the following products: ")
        my_customer.print_orders_placed()
        sys.exit()

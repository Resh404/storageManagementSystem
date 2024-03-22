from productDefinition.product_imp import Product
from storageManagementDatabase.get_data_from_table_in_database import TableDataFletcher
from storageManagementDatabase.connect_to_database import ConnectToDatabase
from productStorage.product_warehouse_imp import Warehouse
from storageManagementDatabase.data_for_database import product_data
import pytest
import random


@pytest.fixture
def warehouse_with_data() -> Warehouse:
    db_connection = ConnectToDatabase(host_name="localhost", user_name="root",
                                      password="Kom12345", port=3306)
    warehouse = Warehouse(location="Test Location", capacity=10000)
    table_data_fletcher = TableDataFletcher()

    # Get table data using TableDataFletcher
    table_data = list(table_data_fletcher.get_table_data(
        "products", db_connection.connect_to_database("storage_database")))

    # Add products to warehouse
    for row in table_data:
        for product_info in row:
            product = Product(*product_info)
            warehouse.add_product(product)

    yield warehouse

    warehouse.products.clear()


@pytest.fixture
def random_entry() -> int:
    return random.randint(5, len(product_data) - 5)


# Test if the method works by editing the length of the data list
# Ensuring the integrity of the fetched data from the database by comparing it against a local copy
def test_add_product_to_warehouse(warehouse_with_data, random_entry):
    fletched_data_validation = warehouse_with_data.products[random_entry]
    product = Product(id=1, name="Test Product", price=10.0, quantity=5, category="Test Category")
    initial_length = len(warehouse_with_data.products)
    warehouse_with_data.add_product(product)

    assert len(warehouse_with_data.products) == initial_length + 1
    assert product in warehouse_with_data.products
    assert fletched_data_validation.name == product_data[random_entry][0]


# Test if the method works by editing the length of the data list
# Ensuring the integrity of the fetched data from the database by comparing it against a local copy
def test_remove_product_from_warehouse(warehouse_with_data, random_entry):
    fletched_data_validation = warehouse_with_data.products[random_entry]
    initial_length = len(warehouse_with_data.products)
    product_to_remove = warehouse_with_data.products[0]
    warehouse_with_data.remove_product(product_to_remove)

    assert len(warehouse_with_data.products) == initial_length - 1
    assert product_to_remove not in warehouse_with_data.products
    assert fletched_data_validation.name == product_data[random_entry][0]


# Test if the method works by editing the name of an entry in the data list
# Ensuring the integrity of the fetched data from the database by comparing it against a local copy
def test_update_product_details_in_warehouse(warehouse_with_data, random_entry):
    fletched_data_validation = warehouse_with_data.products[random_entry]
    product_to_update = warehouse_with_data.products[0]
    original_name = product_to_update.name
    updated_name = "Updated Product"
    warehouse_with_data.update_product_details(product_to_update.id, name=updated_name)

    assert product_to_update.name == updated_name
    assert fletched_data_validation.name == product_data[random_entry][0]

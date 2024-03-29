import pytest
import random
from productDefinition.product_imp import Product
from storageManagementDatabase.get_data_from_table_in_database import TableDataFletcher
from storageManagementDatabase.connect_to_database import ConnectToDatabase
from productStorage.product_inventory_imp import Inventory
from storageManagementDatabase.data_for_database import product_data


@pytest.fixture
def inventory_with_data() -> Inventory:
    inventory = Inventory()

    # Get table data using TableDataFletcher
    table_data = list(TableDataFletcher.get_table_data("products"))

    # Add products to inventory
    for row in table_data:
        for product_info in row:
            product = Product(*product_info)
            inventory.add_product(product)

    yield inventory

    inventory.products.clear()


@pytest.fixture
def random_entry() -> int:
    return random.randint(5, len(product_data) - 5)


# Test if the method works by editing the length of the data list
# Ensuring the integrity of the fletched data from the database by comparing it against a local copy
def test_add_product(inventory_with_data, random_entry):
    fletched_data_validation = inventory_with_data.products[random_entry]
    product = Product(id=1, name="Test Product", price=10.0, quantity=5, category="Test Category")
    initial_length = len(inventory_with_data.products)
    inventory_with_data.add_product(product)

    assert len(inventory_with_data.products) == initial_length + 1
    assert product in inventory_with_data.products
    assert fletched_data_validation.name == product_data[random_entry][0]


# Test if the method works by editing the length of the data list
# Ensuring the integrity of the fletched data from the database by comparing it against a local copy
def test_remove_product(inventory_with_data, random_entry):
    fletched_data_validation = inventory_with_data.products[random_entry]
    initial_length = len(inventory_with_data.products)
    product_to_remove = inventory_with_data.products[0]
    inventory_with_data.remove_product(product_to_remove)

    assert len(inventory_with_data.products) == initial_length - 1
    assert product_to_remove not in inventory_with_data.products
    assert fletched_data_validation.name == product_data[random_entry][0]


# Test if the method works by editing the name of an entry in the data list
# Ensuring the integrity of the fletched data from the database by comparing it against a local copy
def test_update_product_details(inventory_with_data, random_entry):
    fletched_data_validation = inventory_with_data.products[random_entry]
    product_to_update = inventory_with_data.products[0]
    original_name = product_to_update.name
    updated_name = "Updated Product"
    inventory_with_data.update_product_details(product_to_update.id, name=updated_name)

    assert product_to_update.name == updated_name
    assert fletched_data_validation.name == product_data[random_entry][0]

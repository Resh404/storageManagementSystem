import pytest
from productCreationImp.sMS_product_implementation import Product
from productStorageImp.sMS_product_warehouse_implementation import Warehouse
from productSaleImp.sMS_order_implementation import Order


# Set up fixtures
@pytest.fixture
def sample_product():
    return [
        Product(1, "Product 1", 10.0, 100, "Category A"),
        Product(2, "Product 2", 20.0, 50, "Category B"),
        Product(3, "Product 3", 30.0, 200, "Category A")
    ]


@pytest.fixture
def sample_warehouse(sample_product):
    warehouse = Warehouse(location="Sample Location", capacity=1000)
    for product in sample_product:
        warehouse.add_product(product)
    return warehouse


@pytest.fixture
def sample_order(sample_warehouse):
    return Order(id=1, product_names=[], product_quantities=[], warehouse=sample_warehouse)


def test_add_product_to_order(sample_product, sample_order):
    product_to_add = sample_product[0]
    sample_order.add_product(product_to_add.name, 5)

    assert product_to_add.name in sample_order.product_names
    assert 5 in sample_order.product_quantities


def test_remove_product_from_order(sample_product, sample_order):
    product_to_add = sample_product[0]
    sample_order.add_product(product_to_add.name, 5)
    sample_order.remove_product(product_to_add.name)

    assert product_to_add.name not in sample_order.product_names
    assert 5 not in sample_order.product_quantities


def test_reserve_products_from_warehouse(sample_product, sample_warehouse, sample_order):
    product_to_reserve = sample_product[0]
    sample_order.add_product(product_to_reserve.name, 5)
    sample_order.reserve_product_from_warehouse()

    assert len(sample_order.reserved_products_list) == 1

from productCreationImp.sMS_product_implementation import Product
from productSaleImp.sMS_customer_implementation import Customer
from productSaleImp.sMS_order_implementation import Order
from productStorageImp.sMS_product_warehouse_implementation import Warehouse
import pytest


# Set up fixtures
@pytest.fixture
def sample_warehouse():
    warehouse = Warehouse(location="Sample Location", capacity=1000)
    products = [
        Product(id=1, name="Product 1", price=10.0, quantity=10, category="Category A"),
        Product(id=2, name="Product 2", price=20.0, quantity=10, category="Category B"),
        Product(id=3, name="Product 3", price=30.0, quantity=10, category="Category A")
    ]
    for product in products:
        warehouse.add_product(product)
    return warehouse


@pytest.fixture
def sample_order(sample_warehouse):
    return Order(id=1,
                 product_names=[],
                 product_quantities=[],
                 warehouse=sample_warehouse)


@pytest.fixture
def sample_customer(sample_order, sample_warehouse):
    for product in sample_warehouse.products:
        sample_order.add_product(product.name, product.quantity)

    return Customer(id=1, name="Sample Customer", orders_placed=sample_order)


def test_calculate_total_cost(sample_order, sample_customer):
    assert sample_customer.calculate_total_cost() == 600


def test_place_order(sample_order, sample_customer):
    initial_order_count = len(sample_customer.orders_being_processed)
    sample_customer.place_order()
    assert len(sample_customer.orders_being_processed) == initial_order_count + 1


def test_cancel_order(sample_order, sample_customer):
    sample_customer.place_order()
    assert len(sample_customer.orders_being_processed) == 1

    sample_customer.cancel_order(sample_customer.orders_being_processed[0])
    assert len(sample_customer.orders_being_processed) == 0


def test_print_orders_placed(capsys, sample_order, sample_customer):
    sample_customer.place_order()
    sample_customer.print_orders_placed()
    captured = capsys.readouterr()

    assert "Product 1" in captured.out
    assert "Product 2" in captured.out
    assert "Product 3" in captured.out

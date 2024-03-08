from productCreationImp.sMS_product_implementation import Product
from productSaleImp.sMS_customer_implementation import Customer
from productSaleImp.sMS_order_implementation import Order
import pytest


# Set up fixtures
@pytest.fixture
def sample_order():
    return Order(id=1,
                 products=[
                     Product(1, "Product 1", 10.0, 100, "Category A"),
                     Product(2, "Product 2", 20.0, 50, "Category B"),
                     Product(3, "Product 3", 30.0, 200, "Category A")
                 ])


@pytest.fixture
def sample_customer(sample_order):
    return Customer(id=1, name="Sample Customer", orders_placed=[sample_order])


def test_calculate_total_cost(sample_order, sample_customer):
    assert sample_customer.calculate_total_cost(sample_customer.orders_placed) == 60.0


def test_place_order(sample_order, sample_customer):
    initial_order_count = len(sample_customer.orders_placed)
    new_order = Order(id=2, products=[])
    sample_customer.place_order(new_order)

    assert len(sample_customer.orders_placed) == initial_order_count + 1
    assert new_order in sample_customer.orders_placed


def test_cancel_order(sample_order, sample_customer):
    initial_order_count = len(sample_customer.orders_placed)
    new_order = Order(id=2, products=[])
    sample_customer.place_order(new_order)

    assert len(sample_customer.orders_placed) == initial_order_count + 1

    sample_customer.cancel_order(new_order)

    assert len(sample_customer.orders_placed) == initial_order_count


def test_print_orders_placed(capsys, sample_order, sample_customer):
    sample_customer.print_orders_placed()
    captured = capsys.readouterr()

    assert str(sample_order) in captured.out

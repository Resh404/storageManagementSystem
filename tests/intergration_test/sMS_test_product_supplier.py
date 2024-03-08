import pytest
from productCreationImp.sMS_product_implementation import Product
from productStorageImp.sMS_product_warehouse_implementation import Warehouse
from productStorageImp.sMS_product_supplier_implementation import Supplier


# Setup fixtures
@pytest.fixture
def sample_product():
    return [
        Product(1, "Product 1", 10.0, 100, "Category A"),
        Product(2, "Product 2", 20.0, 50, "Category B"),
        Product(3, "Product 3", 30.0, 200, "Category A")
    ]


@pytest.fixture
def sample_warehouse():
    return Warehouse(location="Sample Location", capacity=10000)


@pytest.fixture
def sample_supplier():
    return Supplier(id=1, name="Sample Supplier", contact_details="123456789", products_supplied=[])


def test_add_product_to_supplier(sample_product, sample_supplier):
    """Test adding a product to a supplier."""
    sample_prod = Product(4, "Product 4", 15.0, 20, "Category A")
    sample_supplier.add_product(sample_prod)

    assert sample_prod in sample_supplier.products_supplied
    assert len(sample_supplier.products_supplied) == 1


def test_remove_product_from_supplier(sample_product, sample_supplier):
    """Test removing a product from a supplier."""
    sample_supplier.add_product(sample_product[0])
    sample_supplier.remove_product(sample_product[0])

    assert sample_product[0] not in sample_supplier.products_supplied
    assert len(sample_supplier.products_supplied) == 0


def test_deliver_supplies_to_warehouse(sample_product, sample_warehouse, sample_supplier):
    """Test delivering supplies from a supplier to a warehouse."""
    sample_supplier.add_product(sample_product[0])
    sample_supplier.deliver_supplies(sample_warehouse)

    assert sample_product[0] in sample_warehouse.products

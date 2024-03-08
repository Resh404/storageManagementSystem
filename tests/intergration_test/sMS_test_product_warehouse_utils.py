import pytest
from your_module_path import WarehouseUtils, Warehouse, Product

# Set up fixtures if needed
@pytest.fixture
def sample_product():
    return Product(id=1, name="Sample Product", price=10.0, quantity=5, category="Sample Category")

@pytest.fixture
def sample_warehouse(sample_product):
    warehouse = Warehouse(location="Sample Location", capacity=10)
    warehouse.products.append(sample_product)
    return warehouse

# Integration test for WarehouseUtils class
def test_warehouse_utils_integration(sample_product, sample_warehouse):
    # Test validate_product method
    assert WarehouseUtils.validate_product(sample_product)

    # Test check_available_space method
    assert WarehouseUtils.check_available_space(sample_warehouse)

    # Test is_product_in_warehouse method
    assert WarehouseUtils.look_up_product_in_warehouse_by_id(sample_product, sample_warehouse)

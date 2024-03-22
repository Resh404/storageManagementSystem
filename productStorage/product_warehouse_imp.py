from productDefinition.product_imp import Product
from productStorage.product_inventory_imp import Inventory
from productUtils.product_warehouse_utils_imp import WarehouseUtils

''' This class defines a Warehouse and what can be done by a Warehouse.
The Warehouse class inherits from the inventory class because it is a form of inventory.
The initialized parameters defines what a warehouse need to be initialized with.
The names of the methods explains the functionality of the method. '''


class Warehouse(Inventory):
    def __init__(self, location: str, capacity: int):
        super().__init__()
        self.location = location
        self.capacity = capacity
        self.utils = WarehouseUtils

    def return_available_space(self) -> int:
        used_space = sum(product.quantity for product in self.products)
        available_space = self.capacity - used_space
        return available_space

    def add_product(self, product: Product) -> bool:
        if not self.utils.validate_product(product):
            print("Invalid product")
            return False

        if not self.utils.check_available_space(self):
            print(f"No space left in the {self.location} warehouse.")
            return False

        self.products.append(product)
        return True

    def remove_product(self, product: Product) -> bool:
        if self.utils.look_up_product_in_warehouse_by_id(product.id, self) is not None:
            self.products.remove(product)
            return True
        return False

    def update_product_details(self, product_id, **kwargs) -> None:
        if self.utils.look_up_product_in_warehouse_by_id(product_id, self) is None:
            print("Product not found.")
            return None

        for product in self.products:
            if product.id == product_id:
                for key, value in kwargs.items():
                    setattr(product, key, value)
                return None

    def get_product_details(self, product_id) -> Product:
        if self.utils.look_up_product_in_warehouse_by_id(product_id, self) is None:
            print("Product not found.")
            return None

        for product in self.products:
            if product.id == product_id:
                return product

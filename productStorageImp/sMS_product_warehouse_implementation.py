from sMS_product_inventory_implementation import Inventory
from productCreationImp.sMS_product_implementation import Product
from productUtilsImp.sMS_product_warehouse_utils_implementation import WarehouseUtils


class Warehouse(Inventory):
    def __init__(self, location: str, capacity: int, utils: WarehouseUtils):
        super().__init__()
        self.location = location
        self.capacity = capacity
        self.utils = utils

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
        print(f"Added product to {self.location} warehouse.")
        return True

    def remove_product(self, product: Product) -> bool:
        if self.utils.is_product_in_warehouse(product, self):
            self.products.remove(product)
            print(f"Removed product from {self.location} warehouse.")
            return True
        return False

    def update_product_details(self, product_id, **kwargs) -> None:
        if not self.utils.is_product_in_warehouse(product_id, self):
            print("Product not found.")
            return None

        for product in self.products:
            if product.id == product_id:
                for key, value in kwargs.items():
                    setattr(product, key, value)
                print("Product updated.")
                return None

    def get_product_details(self, product_id) -> Product:
        if not self.utils.is_product_in_warehouse(product_id, self):
            print("Product not found.")
            return None

        for product in self.products:
            if product.id == product_id:
                return product

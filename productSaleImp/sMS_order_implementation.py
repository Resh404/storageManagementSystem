from productCreationImp.sMS_product_implementation import Product
from productStorageImp.sMS_product_warehouse_implementation import Warehouse
from productUtilsImp.sMS_Iproduct_handler_implementation import ProductHandler
from productUtilsImp.sMS_product_warehouse_utils_implementation import WarehouseUtils
from typing import List


class Order(ProductHandler):

    def __init__(self, id: int, product_names: List['str'], product_quantities: List[int], warehouse: Warehouse):
        self.id = id
        self.product_names = product_names
        self.product_quantities = product_quantities
        self.warehouse = warehouse

        self.utils = WarehouseUtils
        self.products = []
        self.reserved_products_list = []

    def add_product(self, product_name: str, product_quantity: int) -> None:
        the_product = self.utils.look_up_product_in_warehouse_by_name(product_name, self.warehouse)
        the_quantity = the_product.quantity

        if the_product is not None and the_quantity >= product_quantity:
            self.product_names.append(product_name)
            self.product_quantities.append(product_quantity)
            self.products.append(the_product)
            return
        return None

    def remove_product(self, product_name) -> None:
        product_index = self.utils.look_up_product_in_warehouse_by_name(product_name, self.warehouse)
        if product_index is not None:
            # Get the index of the product in product_names list
            index_to_remove = self.product_names.index(product_name)

            # Remove the product name and quantity
            del self.product_names[index_to_remove]
            del self.product_quantities[index_to_remove]
            del self.products[index_to_remove]
            return
        return None

    def reserve_product_from_warehouse(self) -> bool:
        if len(self.product_names) != len(self.product_quantities):
            print("Error: The number of product names and quantities does not match.")
            return False

        for product_name, quantity in zip(self.product_names, self.product_quantities):
            product = self.utils.look_up_product_in_warehouse_by_name(product_name, self.warehouse)
            if product is not None and product.quantity >= quantity:
                reserved_product = Product(product.id, product.name, product.price, quantity, product.category)
                self.reserved_products_list.append(reserved_product)

                # Update the quantity of the product in the warehouse
                product.quantity -= quantity
                if product.quantity <= 0:
                    self.warehouse.remove_product(product)
            else:
                print(f"Error: Insufficient quantity of product '{product_name}' in the warehouse.")
                return False
        return True



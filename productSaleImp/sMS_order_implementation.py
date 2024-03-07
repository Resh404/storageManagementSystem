from productCreationImp.sMS_product_implementation import Product
from productStorageImp.sMS_product_warehouse_implementation import Warehouse
from productUtilsImp.sMS_Iproduct_handler_implementation import ProductHandler
from typing import List


class Order(ProductHandler):

    def __init__(self, id: int, products: List['Product']):
        self.id = id
        self.products = products
        self.reserved_products_list = []

    def add_product(self, product: Product) -> None:
        self.products.append(product)

    def remove_product(self, product: Product) -> None:
        self.products.remove(product)

    def reserve_product_from_warehouse(self, product_names: List[str], quantities: List[int],
                                       warehouse: Warehouse) -> bool:
        for prod_name, quantity in zip(product_names, quantities):
            # Find the product in warehouse
            print(warehouse.products)
            found = False
            for product in warehouse.products:
                if product.name.lower() == prod_name.lower():
                    if product.quantity >= quantity:

                        reserved_product = Product(product.id, product.name, product.price, quantity, product.category)
                        self.reserved_products_list.append(reserved_product)
                        product.quantity -= quantity
                        # Check if the product needs to be removed from the warehouse
                        if product.quantity <= 0:
                            warehouse.remove_product(product)
                        found = True
                        break
                    else:
                        print(f"Desired quantity of product with ID {prod_name} not available")
                        return False
            if not found:
                print(f"Product ID {prod_name} not found in the warehouse")
                return False
        return True

    def __str__(self) -> str:
        product_list = []
        total_cost = 0
        for product in self.products:
            product_info = f"{product.name}, Quantity: {product.quantity}, Price: ${product.price:.2f}"
            product_list.append(product_info)
            total_cost += product.price * product.quantity
        product_str = '\n'.join(product_list)
        return f"Products:\n{product_str}\nTotal Cost: ${total_cost:.2f}"



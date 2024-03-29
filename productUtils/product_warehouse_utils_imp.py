from productDefinition.product_imp import Product

''' This class is intended as a utility class that provides additional functionality for the classes that needs
to interact with products or warehouse, thus simplify those classes and their methods.
The names of the methods explains the functionality of the method. '''


class WarehouseUtils:
    @staticmethod
    def validate_product(product: Product) -> bool:
        if not isinstance(product, Product) or product is None:
            return False
        return True

    @staticmethod
    def check_available_space(warehouse) -> bool:
        if warehouse.return_available_space() <= 0:
            return False
        return True

    @staticmethod
    def look_up_product_in_warehouse_by_id(product_id_look_up: int, warehouse) -> Product:
        for product in warehouse.products:
            if product.id == product_id_look_up:
                return product
        return None

    @staticmethod
    def look_up_product_in_warehouse_by_name(product_name_look_up: str, warehouse) -> Product:
        for product in warehouse.products:
            if product.name.lower() == product_name_look_up.lower():
                return product
        return None

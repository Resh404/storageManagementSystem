from productCreationImp.sMS_product_implementation import Product


# Utils methods for the storage management system. Can be expanded
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
    def is_product_in_warehouse(product: Product, warehouse) -> bool:
        for item in warehouse.products:
            if item.id == product.id:
                return True
        return False

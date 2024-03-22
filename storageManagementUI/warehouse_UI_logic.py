from storageManagementDatabase.get_data_from_table_in_database import TableDataFletcher
from productStorage.product_warehouse_imp import Warehouse
from storageManagementFactory.product_storage_factory import StorageFactory

''' This class contains the logic that allows the user to see the products in a warehouse. 
The names of the methods explains the functionality of the method. '''


class WarehouseChoices:
    @staticmethod
    def display_warehouse_products() -> Warehouse:
        aarhus_warehouse = StorageFactory.create_warehouse("Aarhus", 10000)
        print(
            f"{aarhus_warehouse.location} warehouse got capacity of: "
            f"{aarhus_warehouse.capacity} and the following products: ")

        for batch in TableDataFletcher.get_table_data("products"):
            for prod in batch:
                product = StorageFactory.create_product(*prod)
                aarhus_warehouse.add_product(product)
                print(str(product))
        return aarhus_warehouse

    @staticmethod
    def display_warehouse_products_by_category(category: str) -> Warehouse:
        aarhus_warehouse = StorageFactory.create_warehouse("Aarhus", 10000)

        for batch in TableDataFletcher.get_table_data("products"):
            for prod in batch:
                product = StorageFactory.create_product(*prod)

                if product.category.lower() == category.lower():
                    aarhus_warehouse.add_product(product)
                    print(str(product))
                    continue
        return aarhus_warehouse

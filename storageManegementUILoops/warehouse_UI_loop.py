import sys

from storageManagementUI.warehouse_UI_logic import WarehouseChoices

''' This class contains the warehouse options a customer is presented with when the system is running.'''


class WarehouseUILoop:
    @staticmethod
    def warehouse_options():
        while True:
            print("1: Show all products\n"
                  "2: show products within a category\n"
                  "3: Exit")
            product_display = input("Enter your choice: ")

            if product_display == '1':
                the_complete_warehouse = WarehouseChoices.display_warehouse_products()
                return the_complete_warehouse
            elif product_display == '2':
                category_map = {
                    '1': "food",
                    '2': "drink",
                    '3': "clothing",
                    '4': "electronics"
                }

                print("Which category?")
                print("1: Food\n"
                      "2: Drink\n"
                      "3: Clothing\n"
                      "4: Electronics")
                category_choice = input("Enter your choice: ")
                category_name = category_map.get(category_choice)

                if category_name in ['food', 'drink', 'clothing', 'electronics']:
                    the_warehouse_sorted = WarehouseChoices.display_warehouse_products_by_category(category_name)
                    return the_warehouse_sorted
                else:
                    print("Invalid category choice")
                    continue
            elif product_display == '3':
                print("Thank you for visiting. Goodbye!")
                sys.exit()
            else:
                print("Invalid input, please try again")
                continue

from storageManagementFactory.product_sale_factory import SaleFactory
from storageManagementUIUtils.UI_utils import UtilsForUI
from storageManegementUILoops.customer_UI_loop import CustomerUILoop
from storageManegementUILoops.order_UI_loop import OrderUILoop
from storageManegementUILoops.warehouse_UI_loop import WarehouseUILoop

''' This class sets together the UI loop from customer_UI_loop, order_UI_loop, and warehouse_UI_loop together 
to create the main loop a user will be able to interact with. '''


class UILoop:
    @staticmethod
    def main_loop():
        print("Welcome to the store!")

        while True:
            customer_mail = CustomerUILoop.customer_options()
            if customer_mail is not None:
                break
        customer_info_in_database = UtilsForUI.check_if_customer_exists(customer_mail)

        the_warehouse = WarehouseUILoop.warehouse_options()
        the_order = SaleFactory.create_order(customer_info_in_database[0], [],
                                             [], the_warehouse)
        the_customer = SaleFactory.create_customer(*customer_info_in_database[:3], the_order)

        while True:
            status = OrderUILoop.order_options(the_customer, the_order)
            if status:
                break

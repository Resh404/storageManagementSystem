from productSaleImp.sMS_order_implementation import Order
from abc import ABC, abstractmethod


class OrderHandler(ABC):

    @abstractmethod
    def place_order(self, order: Order):
        pass

    @abstractmethod
    def cancel_order(self, order: Order):
        pass

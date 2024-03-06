from abc import ABC, abstractmethod
from productSaleImp.sMS_order_implementation import Order


class OrderHandler(ABC):

    @abstractmethod
    def place_order(self, order: Order):
        pass

    @abstractmethod
    def cancel_order(self, order: Order):
        pass

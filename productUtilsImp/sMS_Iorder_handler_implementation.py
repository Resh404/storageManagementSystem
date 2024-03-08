from abc import ABC, abstractmethod


class OrderHandler(ABC):

    @abstractmethod
    def place_order(self, *args, **kwargs):
        pass

    @abstractmethod
    def cancel_order(self, *args, **kwargs):
        pass

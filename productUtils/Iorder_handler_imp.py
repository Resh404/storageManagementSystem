from abc import ABC, abstractmethod

''' This class is intended as a interface class for classes that uses an order logic such as the customer class.
The interface defines methods that must be implemented by the classes which implement this interface.
The names of the methods explains the functionality of the method. '''


class OrderHandler(ABC):

    @abstractmethod
    def place_order(self, *args, **kwargs):
        pass

    @abstractmethod
    def cancel_order(self, *args, **kwargs):
        pass

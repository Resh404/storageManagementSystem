from abc import ABC, abstractmethod

''' This class is intended as a interface class for classes that uses an product logic such as the 
order, warehouse, supplier and more classes.
The interface defines methods that must be implemented by the classes which implement this interface.
The names of the methods explains the functionality of the method. '''


class ProductHandler(ABC):
    @abstractmethod
    def add_product(self, *args, **kwargs) -> None:
        pass

    @abstractmethod
    def remove_product(self, *args, **kwargs) -> None:
        pass

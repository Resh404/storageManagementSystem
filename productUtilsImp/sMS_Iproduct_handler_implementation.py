from productCreationImp.sMS_product_implementation import Product
from abc import ABC, abstractmethod


class ProductHandler(ABC):
    @abstractmethod
    def add_product(self, *args, **kwargs) -> None:
        pass

    @abstractmethod
    def remove_product(self, *args, **kwargs) -> None:
        pass
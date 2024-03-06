from productCreationImp.sMS_product_implementation import Product
from abc import ABC, abstractmethod


class ProductHandler(ABC):
    @abstractmethod
    def add_product(self, product: Product) -> None:
        pass

    @abstractmethod
    def remove_product(self, product: Product) -> None:
        pass
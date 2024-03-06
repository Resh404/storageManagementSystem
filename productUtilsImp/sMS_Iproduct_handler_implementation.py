from abc import ABC, abstractmethod
from productCreationImp.sMS_product_implementation import Product


class ProductHandler(ABC):
    @abstractmethod
    def add_product(self, product: Product) -> None:
        pass

    @abstractmethod
    def remove_product(self, product: Product) -> None:
        pass
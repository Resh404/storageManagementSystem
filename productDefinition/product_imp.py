

''' This class defines a product, the products parameters, and the type of the parameters.
Getters and setters are used to retrieve and set information about the product if needed.
The name of the parameters entails its function. '''


class Product:
    def __init__(self, id: int, name: str, price: float, quantity: int, category: str):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category

    # setters and getters for the parameters of the class
    @property
    def item_id(self) -> int:
        return self.id

    @property
    def item_name(self) -> str:
        return self.name

    @property
    def item_price(self) -> float:
        return self.price

    @property
    def item_quantity(self) -> int:
        return self.quantity

    @property
    def item_category(self) -> str:
        return self.category

    @item_id.setter
    def item_id(self, new_id: int) -> None:
        self.id = new_id

    @item_name.setter
    def item_name(self, new_name: str) -> None:
        self.name = new_name

    @item_price.setter
    def item_price(self, new_price: float) -> None:
        self.price = new_price

    @item_quantity.setter
    def item_quantity(self, new_quantity: int) -> None:
        self.quantity = new_quantity

    @item_category.setter
    def item_category(self, new_category: str) -> None:
        self.category = new_category

    # return a string representation and not just references
    def __str__(self):
        return f"Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}, Category: {self.category}"

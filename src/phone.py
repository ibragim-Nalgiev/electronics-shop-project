from src.item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        if type(value) != int or value <= 0:
            raise ValueError
        self.__number_of_sim = value

    def __add__(self, other):
        if not isinstance(other, (Phone, Item)):
            raise ValueError("можно складывать только объекты класса Phone или Item")
        return self.quantity + other.quantity

    def __radd__(self, other):
        return self.quantity + other.quantity

    def __repr__(self):
        return f"Phone{self.name, self.price, self.quantity, self.number_of_sim}"

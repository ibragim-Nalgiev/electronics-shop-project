import csv
from src.csverror import InstantiateCSVError

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)


    @property
    def name(self) -> str:
        """Возвращает название товара"""
        return self.__name

    @name.setter
    def name(self, new_name: str) -> None:
        """Присваивает название товару"""
        if self.validate_name(new_name):
            self.__name = new_name
        else:
            raise ValueError("Длина наименования товара превышает 10 символов.")

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price


    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate
        return self.price


    @classmethod
    def validate_name(cls, name: str) -> int:
        """Проверка названия на длину"""
        return len(name) <= 10

    @classmethod
    def instantiate_from_csv(cls, path: str ="../src/items.csv") -> None:
        """Cоздаем экзепляры класса на основе данных их файла"""
        all_info = []

        try:
            with open(path, encoding="CP1251") as csv_file:
                take_csv_data = csv.reader(csv_file, delimiter=",")
                count = 0
                for i in take_csv_data:
                    if count != 0:
                        all_info.append(i)
                    else:
                        if len(i) != 3:
                            raise InstantiateCSVError

                        count += 1
        except InstantiateCSVError:
            csv_error = InstantiateCSVError()
            print(csv_error)
        except Exception:
            print("Отсутствует файл item.csv")

        for data in all_info:
            cls(*data)

    @staticmethod
    def string_to_number(number: str) -> int:
        """Cтатический метод, возвращающий число из числа-строки
        :return: Число в нужном нам формате
        """
        return int(number.split(".")[0])
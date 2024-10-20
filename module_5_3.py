class House:
    def __init__(self, name, number_of_floors):
        """
        Инициализирует объект House с именем и количеством этажей.

        :param name: Название дома
        :param number_of_floors: Количество этажей в доме
        """
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):
        """Возвращает строковое представление объекта House."""
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        """Возвращает True, если количество этажей одинаковое."""
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return False

    def __ne__(self, other):
        """Возвращает True, если количество этажей различается."""
        return not self.__eq__(other)

    def __lt__(self, other):
        """Возвращает True, если этажей меньше."""
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return NotImplemented

    def __le__(self, other):
        """Возвращает True, если этажей меньше или равно."""
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        return NotImplemented

    def __gt__(self, other):
        """Возвращает True, если этажей больше."""
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return NotImplemented

    def __ge__(self, other):
        """Возвращает True, если этажей больше или равно."""
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        return NotImplemented

    def __add__(self, value):
        """Увеличивает количество этажей на значение value и возвращает новый объект."""
        if isinstance(value, int):
            return House(self.name, self.number_of_floors + value)
        return NotImplemented

    def __radd__(self, value):
        """Работает как __add__ для других классов."""
        return self.__add__(value)

    def __iadd__(self, value):
        """Увеличивает количество этажей на значение value и возвращает объект."""
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        return NotImplemented


# Пример использования
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)  # Название: ЖК Эльбрус, кол-во этажей: 10
print(h2)  # Название: ЖК Акация, кол-во этажей: 20

print(h1 == h2)  # False

h1 = h1 + 10  # Увеличиваем на 10
print(h1)  # Название: ЖК Эльбрус, кол-во этажей: 20
print(h1 == h2)  # True

h1 += 10  # Увеличиваем на 10
print(h1)  # Название: ЖК Эльбрус, кол-во этажей: 30

h2 = 10 + h2  # Увеличиваем на 10
print(h2)  # Название: ЖК Акация, кол-во этажей: 30

print(h1 > h2)  # False
print(h1 >= h2)  # True
print(h1 < h2)  # False
print(h1 <= h2)  # True
print(h1 != h2)  # False

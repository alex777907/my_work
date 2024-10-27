class House:
    houses_history = []  # Атрибут класса для хранения истории домов

    def __new__(cls, *args, **kwargs):
        """
        Метод __new__ вызывается перед __init__ и отвечает за создание нового объекта.
        Здесь мы добавляем название дома в историю.
        """
        if args:
            name = args[0]  # Предполагаем, что имя дома первое в аргументах
            cls.houses_history.append(name)
        return super().__new__(cls)

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
        """Работает как add для других классов."""
        return self.__add__(value)

    def __iadd__(self, value):
        """Увеличивает количество этажей на значение value и возвращает объект."""
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        return NotImplemented

    def __del__(self):
        """Выводит сообщение при удалении объекта."""
        print(f"{self.name} снесён, но он останется в истории")
# Создание объектов
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)  # Ожидается: ['ЖК Эльбрус']

h2 = House('ЖК Акация', 20)
print(House.houses_history)  # Ожидается: ['ЖК Эльбрус', 'ЖК Акация']

h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)  # Ожидается: ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']

# Удаление объектов
del h2  # Ожидается вывод: ЖК Акация снесён, но он останется в истории
del h3  # Ожидается вывод: ЖК Матрёшки снесён, но он останется в истории

print(House.houses_history)  # Ожидается: ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']

del h1  # Ожидается вывод: ЖК Эльбрус снесён, но он останется в истории

print(House.houses_history)  # Ожидается: ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']

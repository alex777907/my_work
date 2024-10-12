class House:
    def __init__(self, name, number_of_floors):
        """
        Инициализирует объект House с именем и количеством этажей.

        :param name: Название дома
        :param number_of_floors: Количество этажей в доме
        """
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        """
        Переходит на указанный этаж, выводя числа от 1 до new_floor.
        Если этаж недействителен, выводит соответствующее сообщение.

        :param new_floor: Номер этажа для перехода
        """
        if 1 <= new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print("Такого этажа не существует")

    def __len__(self):
        """
        Возвращает количество этажей в доме.

        :return: Количество этажей
        """
        return self.number_of_floors

    def __str__(self):
        """
        Возвращает строковое представление объекта House.

        :return: Строка с названием и количеством этажей
        """
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

# Создаем объект дома с названием 'ЖК Эльбрус' и 30 этажами
my_house = House('ЖК Эльбрус', 30)

# Используем метод go_to
print("Переход на 5-й этаж:")
my_house.go_to(5)

print("\nПереход на 31-й этаж:")
my_house.go_to(31)

print("\nПереход на 0-й этаж:")
my_house.go_to(0)

# Используем специальный метод __len__
print(f"\nКоличество этажей в доме: {len(my_house)}")

# Используем специальный метод __str__
print(f"\nИнформация о доме: {my_house}")

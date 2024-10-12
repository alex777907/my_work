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

# Создаем объект дома с названием 'ЖК Эльбрус' и 30 этажами
my_house = House('ЖК Эльбрус', 30)

# Пытаемся перейти на 5-й этаж
print("Переход на 5-й этаж:")
my_house.go_to(5)

# Пытаемся перейти на 31-й этаж (не существует)
print("\nПереход на 31-й этаж:")
my_house.go_to(31)

# Пытаемся перейти на 0-й этаж (не существует)
print("\nПереход на 0-й этаж:")
my_house.go_to(0)


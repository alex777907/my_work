import math

# Базовый класс Figure
class Figure:
    def __init__(self, color, *sides):
        self._sides = []  # Публичный атрибут
        self._color = color
        self.filled = False
        self.set_sides(*sides)  # Устанавливаем стороны через сеттер

    # Геттер для получения цвета
    def get_color(self):
        return self._color

    # Проверка валидности цвета
    def __is_valid_color(self, r, g, b):
        return all(0 <= x <= 255 for x in [r, g, b])

    # Сеттер для изменения цвета
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self._color = [r, g, b]

    # Геттер для получения сторон
    def get_sides(self):
        return self._sides

    # Проверка валидности сторон
    def __is_valid_sides(self, *new_sides):
        if len(new_sides) != self.sides_count:
            return False
        return all(isinstance(x, int) and x > 0 for x in new_sides)

    # Сеттер для изменения сторон
    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self._sides = list(new_sides)

    # Метод для периметра (длина фигуры)
    def __len__(self):
        return sum(self._sides)

# Класс Circle (круг)
class Circle(Figure):
    sides_count = 1  # У круга только одна "сторона" - длина окружности

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(self.get_sides()) == 1:
            self.__radius = self.get_sides()[0] / (2 * math.pi)
        else:
            self.__radius = 0

    # Геттер для радиуса
    def get_radius(self):
        return self.__radius

    # Площадь круга
    def get_square(self):
        return math.pi * self.__radius ** 2

# Класс Triangle (треугольник)
class Triangle(Figure):
    sides_count = 3  # У треугольника три стороны

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    # Площадь треугольника по формуле Герона
    def get_square(self):
        a, b, c = self.get_sides()
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))

# Класс Cube (куб)
class Cube(Figure):
    sides_count = 12  # У куба 12 рёбер

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

        # Если передано 1 значение, делаем все 12 рёбер одинаковыми
        if len(self.get_sides()) == 1:
            self._sides = [self.get_sides()[0]] * 12
        # Если передано меньше 12 сторон, заполняем их единицами
        elif len(self.get_sides()) < 12:
            self._sides = self.get_sides() + [6] * (12 - len(self.get_sides()))
        elif len(self.get_sides()) == 12:
            self._sides = self.get_sides()

    # Объем куба
    def get_volume(self):
        if self.get_sides():
            side = self.get_sides()[0]  # Получаем размер рёбер
            return side ** 3  # Объем куба = сторона^3
        return 0

    # Переопределяем геттер сторон, чтобы гарантировать доступ к 12 рёбрам
    def get_sides(self):
        return self._sides

# Пример использования

circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())  # [55, 66, 77]

cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())  # [222, 35, 130]

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())  # [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]

circle1.set_sides(15)  # Изменится
print(circle1.get_sides())  # [15]

# Проверка периметра (круга), это и есть длина:
print(len(circle1))  # 15

# Проверка объёма (куба):
print(cube1.get_volume())  # 216

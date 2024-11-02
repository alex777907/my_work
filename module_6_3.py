class Horse:
    def __init__(self):
        self.x_distance = 0  # Пройденный путь по оси X
        self.sound = 'Frrr'  # Звук, который издаёт лошадь

    def run(self, dx):
        """Увеличивает x_distance на dx."""
        self.x_distance += dx


class Eagle:
    def __init__(self):
        self.y_distance = 0  # Высота полёта по оси Y
        self.sound = 'I train, eat, sleep, and repeat'  # Звук, который издаёт орёл

    def fly(self, dy):
        """Увеличивает y_distance на dy."""
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    def __init__(self):
        Horse.__init__(self)  # Инициализация атрибутов Horse
        Eagle.__init__(self)  # Инициализация атрибутов Eagle

    def move(self, dx, dy):
        """Запускает методы run и fly для изменения дистанции."""
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        """Возвращает текущие координаты (x_distance, y_distance)."""
        return (self.x_distance, self.y_distance)

    def voice(self):
        """Печатает звук, унаследованный от класса Eagle."""
        print(self.sound)


# Пример работы программы
if __name__ == "__main__":
    p1 = Pegasus()

    print(p1.get_pos())      # Ожидается: (0, 0)
    p1.move(10, 15)
    print(p1.get_pos())      # Ожидается: (10, 15)
    p1.move(-5, 20)
    print(p1.get_pos())      # Ожидается: (5, 35)

    p1.voice()               # Ожидается: I train, eat, sleep, and repeat

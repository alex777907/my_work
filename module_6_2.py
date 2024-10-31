class Vehicle:
    # Атрибут класса: допустимые цвета (приватный)
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner  # Владелец транспорта (может меняться)
        self.__model = model  # Модель транспорта (приватный)
        self.__color = color  # Цвет транспорта (приватный)
        self.__engine_power = engine_power  # Мощность двигателя (приватный)

    def get_model(self):
        """Возвращает модель транспорта."""
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        """Возвращает мощность двигателя."""
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        """Возвращает цвет транспорта."""
        return f"Цвет: {self.__color}"

    def print_info(self):
        """Печатает информацию о транспорте."""
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color):
        """
        Изменяет цвет транспорта на new_color, если он допустим.
        Иначе выводит сообщение о невозможности смены цвета.
        Проверка не учитывает регистр.
        """
        # Преобразуем оба цвета в нижний регистр для сравнения
        allowed_colors = [color.lower() for color in self.__COLOR_VARIANTS]
        if new_color.lower() in allowed_colors:
            # Находим оригинальный регистр цвета из допустимых вариантов
            index = allowed_colors.index(new_color.lower())
            original_color = self.__COLOR_VARIANTS[index]
            self.__color = original_color  # Сохраняем цвет с оригинальным регистром
        else:
            print(f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle):
    # Атрибут класса: ограничение на количество пассажиров (приватный)
    __PASSENGERS_LIMIT = 5

    def get_passengers_limit(self):
        """Возвращает ограничение на количество пассажиров."""
        return f"Лимит пассажиров: {self.__PASSENGERS_LIMIT}"


# Создание объектов классов и проверка работы методов
if __name__ == "__main__":
    # Создание объекта класса Sedan
    vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

    # Изначальные свойства
    vehicle1.print_info()

    # Меняем свойства (в т.ч. вызывая методы)
    vehicle1.set_color('Pink')     # Пытаемся сменить на недопустимый цвет
    vehicle1.set_color('BLACK')    # Смена на допустимый цвет (регистронезависимо)
    vehicle1.owner = 'Vasyok'      # Изменяем владельца

    # Проверяем, что поменялось
    vehicle1.print_info()

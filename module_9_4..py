from random import choice

# Часть 1: lambda-функция для сравнения строк
first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda x, y: x == y, first, second))
print(result)  # [False, True, True, False, False, False, False, False, True, False, False, False, False, False]

# Часть 2: Класс MysticBall с методом __call__
class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())  # может вернуть 'Да'
print(first_ball())  # может вернуть 'Нет'
print(first_ball())  # может вернуть 'Наверное'

# Часть 3: Замыкание для записи в файл
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            for data in data_set:
                file.write(str(data) + '\n')
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

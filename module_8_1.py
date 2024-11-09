def add_everything_up(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b  # Сложение чисел
    elif isinstance(a, str) and isinstance(b, str):
        return a + b  # Конкатенация строк
    else:
        # Если типы разные, то возвращаем строковое представление в том же порядке
        return str(a) + str(b)


print(add_everything_up(123.456, 'строка'))  # 123.456строка
print(add_everything_up('яблоко', 4215))    # яблоко4215
print(add_everything_up(123.456, 7))        # 130.456

def get_multiplied_digits(number):
    # Преобразуем число в строку
    str_number = str(number)

    # Если длина строки больше 1, продолжаем рекурсию
    if len(str_number) > 1:
        first = int(str_number[0])  # Получаем первую цифру
        # Если первая цифра равна 0, пропускаем её
        if first == 0:
            return get_multiplied_digits(int(str_number[1:]))
        # Умножаем первую цифру на результат рекурсивного вызова для остальных цифр
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        # Если длина строки равна 1, просто возвращаем первую цифру, если она не ноль
        return int(str_number[0]) if str_number[0] != '0' else 1  # Возвращаем 1, если цифра 0


# Пример использования
result = get_multiplied_digits(40203)
print(result) # Вывод: 24 (4 * 2 * 3)

result_zero_ending = get_multiplied_digits(420)
print(result_zero_ending)  # Вывод: 8 (4 * 2)

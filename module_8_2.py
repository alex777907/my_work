def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for item in numbers:
        try:
            if isinstance(item, (int, float)):  # Проверяем, является ли элемент числом
                result += item
            else:
                raise TypeError  # Генерируем исключение, если элемент не число
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {item}')
    return result, incorrect_data


def calculate_average(numbers):
    if not isinstance(numbers, (list, tuple)):  # Проверяем, является ли numbers коллекцией
        print('В numbers записан некорректный тип данных')
        return None

    total_sum, incorrect_data = personal_sum(numbers)

    if len(numbers) == 0:  # Обрабатываем случай с пустой коллекцией
        return 0

    return total_sum / (len(numbers) - incorrect_data)  # Учитываем только корректные данные


# Пример вызова функций:

print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')

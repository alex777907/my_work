def apply_all_func(int_list, *functions):
    # Создаем пустой словарь для хранения результатов
    results = {}

    # Перебираем все функции
    for func in functions:
        # Получаем имя функции и применяем её к списку
        result = func(int_list)
        # Записываем результат в словарь
        results[func.__name__] = result

    return results

# Пример использования:
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

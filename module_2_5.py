def get_matrix(n, m, value):
    # Создаем пустой список для матрицы
    matrix = []

    # Внешний цикл для количества строк
    for i in range(n):
        # Создаем пустую строку
        row = []

        # Внутренний цикл для количества столбцов
        for j in range(m):
            # Заполняем строку значением
            row.append(value)

        # Добавляем строку в матрицу
        matrix.append(row)

    # Возвращаем созданную матрицу
    return matrix


# Пример использования функции
result_matrix = get_matrix(5, 4, 4)

# Выводим результат на экран
print(result_matrix)

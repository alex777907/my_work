first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Первая генераторная сборка: разница длин строк, если длины не равны
first_result = (abs(len(f) - len(s)) for f, s in zip(first, second) if len(f) != len(s))

# Вторая генераторная сборка: сравнение длин строк на одинаковых позициях, без использования zip
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

# Выводим результаты
print(list(first_result))
print(list(second_result))

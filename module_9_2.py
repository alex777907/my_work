first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# Первая часть: список длин строк, где длина строки >= 5
first_result = [len(s) for s in first_strings if len(s) >= 5]

# Вторая часть: список кортежей из всех комбинаций строк из first_strings и second_strings
second_result = [(f, s) for f in first_strings for s in second_strings]

# Третья часть: словарь, где ключ - строка, значение - длина строки, только если длина строки чётная
third_result = {s: len(s) for s in first_strings + second_strings if len(s) % 2 == 0}

# Вывод результатов
print(first_result)
print(second_result)
print(third_result)

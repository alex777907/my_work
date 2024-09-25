# Переменная для подсчёта количества вызовов
calls = 0

# Функция для подсчета вызовов
def count_calls():
    global calls
    calls += 1

# Функция, которая принимает строку и возвращает ее характеристики
def string_info(string):
    count_calls()  # Увеличиваем счётчик вызовов
    return (len(string), string.upper(), string.lower())

# Функция, проверяющая наличие строки в списке
def is_contains(string, list_to_search):
    count_calls()  # Увеличиваем счётчик вызовов
    return string.lower() in (item.lower() for item in list_to_search)

# Примеры вызовов функций
info1 = string_info("Hello World")
info2 = string_info("Python Programming")
contains1 = is_contains("urban", ["New York", "London", "URBAN"])
contains2 = is_contains("Python", ["Java", "C++", "Ruby"])

# Вывод результата работы функций
print("('Hello World'):", info1)
print("('Python Programming'):", info2)
print("('urban', ['New York', 'London', 'URBAN']):", contains1)
print("('Python', ['Java', 'C++', 'Ruby']):", contains2)

# Вывод количества вызовов
print("Количество вызовов функций:", calls)

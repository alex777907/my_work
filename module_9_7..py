# Декоратор для проверки простоты числа
def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)  # Получаем результат работы sum_three
        if result < 2:
            print("Составное")
        else:
            # Проверка, простое ли число
            for i in range(2, int(result ** 0.5) + 1):
                if result % i == 0:
                    print("Составное")
                    return result
            print("Простое")
        return result
    return wrapper

# Функция, которая складывает три числа
@is_prime
def sum_three(a, b, c):
    return a + b + c

# Пример использования
result = sum_three(2, 3, 6)
print(result)

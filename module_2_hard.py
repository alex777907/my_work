import random


def find_pairs(num):
    pairs = []

    # Перебираем возможные значения для a и b
    for a in range(1, 21):
        for b in range(a + 1, 21):
            sum_ab = a + b

            # Проверяем, делится ли num на сумму a и b
            if num % sum_ab == 0:
                pairs.append((a, b))  # Добавляем подходящую пару

    return pairs


# Генерируем случайное число от 3 до 20
random_number = random.randint(3, 20)
print(f"Выбранное число: {random_number}")

# Находим пары
result_pairs = find_pairs(random_number)

# Выводим результат
print("Пары чисел (a, b), для которых", random_number, "кратно (a + b):")
for pair in result_pairs:
    print(pair)

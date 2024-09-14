import random

# Генерируем случайное число от 3 до 20
number_from_first_slot = random.randint(3, 20)
print(f"Число из первого поля: {number_from_first_slot}")

# Инициализация пустой строки для пароля
result = ""

# Ищем пары чисел от 1 до 20
for i in range(1, 21):
    for j in range(i + 1, 21):
        pair_sum = i + j  # Сумма пары
        # Проверяем, кратно ли число первому числу
        if pair_sum != 0 and number_from_first_slot % pair_sum == 0:
            result += f"{i}{j}"  # Конкатенация чисел пары в строку

# Выводим результат
if result:
    print(f"Пароль: {result}")
else:
    print("Не найдено подходящих пар.")

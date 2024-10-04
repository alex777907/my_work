# module_4_1.py

from fake_math import divide as fake_divide
from true_math import divide as true_divide

# Примеры вызова функций
result1 = fake_divide(236, 32)
result2 = fake_divide(321, 0)
result3 = true_divide(50, 70)
result4 = true_divide(15, 0)

# Вывод результатов на экран
print(result1)
print(result2)
print(result3)
print(result4)

class StepValueError(ValueError):
    pass


class Iterator:
    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError('Шаг не может быть равен 0')
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start  # Указатель на текущее значение, изначально равно start

    def __iter__(self):
        self.pointer = self.start  # Сбрасываем указатель на начальное значение
        return self  # Возвращаем сам итератор для использования в цикле

    def __next__(self):
        if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop):
            raise StopIteration  # Завершаем итерацию, когда указатель выходит за пределы диапазона

        current = self.pointer
        self.pointer += self.step  # Обновляем указатель на следующий элемент
        return current


# Пример использования:

try:
    iter1 = Iterator(100, 200, 0)  # Здесь выбрасывается исключение StepValueError
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

print()  # Печатаем пустую строку для разделения результатов

# Для каждого итератора выполняем цикл for
for i in iter2:
    print(i, end=' ')
print()

for i in iter3:
    print(i, end=' ')
print()

for i in iter4:
    print(i, end=' ')
print()

for i in iter5:
    print(i, end=' ')
print()

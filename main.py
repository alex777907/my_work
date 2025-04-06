import matplotlib.pyplot as plt
import numpy as np
import math

def read_data_from_file(filename):
    """Чтение данных из файла"""
    with open(filename, 'r') as file:
        data = file.read().split()
        if len(data) != 9:
            raise ValueError("Файл должен содержать 9 чисел: x1, y1, R1, x2, y2, r2, x3, y3, r3")
        return list(map(float, data))

def check_intersection(x1, y1, r1, x2, y2, r2):
    """Проверка пересечения двух окружностей"""
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return abs(r1 - r2) <= distance <= (r1 + r2)

def draw_circle(ax, x, y, r, color):
    """Рисование окружности"""
    circle = plt.Circle((x, y), r, color=color, fill=False, linewidth=3)
    ax.add_patch(circle)
    ax.plot(x, y, 'o', color=color)

def main():
    # Чтение данных из файла
    filename = 'data.txt'  # Укажите путь к файлу с данными
    x1, y1, R1, x2, y2, r2, x3, y3, r3 = read_data_from_file(filename)

    # Проверка пересечения окружностей
    condition1 = check_intersection(x1, y1, R1, x2, y2, r2)
    condition2 = check_intersection(x2, y2, r2, x3, y3, r3)
    condition3 = check_intersection(x1, y1, R1, x3, y3, r3)

    # Подсчет количества пересекающихся пар
    intersection_count = sum([condition1, condition2, condition3])

    # Проверка условия (ровно две пересекающиеся пары)
    if intersection_count != 2:
        raise ValueError(
            f"Ошибка: пересекаются {intersection_count} пар(ы) окружностей. Должны пересекаться ровно две пары.")

    # Создание фигуры
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_aspect('equal')

    # Определение границ графика
    max_radius = max(R1, r2, r3)
    min_x = min(x1 - R1, x2 - r2, x3 - r3)
    max_x = max(x1 + R1, x2 + r2, x3 + r3)
    min_y = min(y1 - R1, y2 - r2, y3 - r3)
    max_y = max(y1 + R1, y2 + r2, y3 + r3)

    # Добавление небольшого отступа
    padding = max_radius * 0.1
    ax.set_xlim(min_x - padding, max_x + padding)
    ax.set_ylim(min_y - padding, max_y + padding)

    # Рисование окружностей с цветами
    draw_circle(ax, x1, y1, R1, 'blue')
    draw_circle(ax, x2, y2, r2, 'green')
    draw_circle(ax, x3, y3, r3, 'red')

    # Добавление заголовка и сетки
    plt.title('Фигура из трех пересекающихся окружностей')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)

    # Отображение графика
    plt.show()

if __name__ == "__main__":
    main()

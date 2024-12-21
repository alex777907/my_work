import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.days_passed = 0

    def run(self):
        global enemies_left

        print(f"{self.name}, на нас напали!")

        while enemies_left > 0:
            if enemies_left <= self.power:
                enemies_left -= enemies_left
            else:
                enemies_left -= self.power

            self.days_passed += 1
            time.sleep(1)  # Пауза на одну секунду (один день)
            print(f"{self.name} сражается {self.days_passed} день(дня)..., осталось {enemies_left} воинов.")

        print(f"{self.name} одержал победу спустя {self.days_passed} дней(дня)!")

    # Глобальная переменная для отслеживания количества врагов


enemies_left = 100

# Создание и запуск двух рыцарей
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

# Ожидание завершения потоков
first_knight.join()
second_knight.join()

# Сообщение об окончании боев
print("Все битвы закончились!")

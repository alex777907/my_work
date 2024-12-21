import random
import threading
import time


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            with self.lock:
                self.balance += amount
                print(f"Пополнение: {amount}. Баланс: {self.balance}")

                # Разблокируем замок, если баланс >= 500
                if self.balance >= 500 and self.lock.locked():
                    self.lock.release()

            time.sleep(0.001)  # Задержка для имитации скорости выполнения пополнения

    def take(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            with self.lock:
                print(f"Запрос на {amount}")
                if amount <= self.balance:
                    self.balance -= amount
                    print(f"Снятие: {amount}. Баланс: {self.balance}")
                else:
                    print("Запрос отклонён, недостаточно средств")
                    self.lock.acquire()  # Блокировка замка, если недостаточно средств


# Создание объекта класса Bank
bank = Bank()

# Создание и запуск потоков
thread_deposit = threading.Thread(target=bank.deposit)
thread_take = threading.Thread(target=bank.take)

thread_deposit.start()
thread_take.start()

# Ожидание завершения потоков
thread_deposit.join()
thread_take.join()

# Итоговый баланс
print(f"Итоговый баланс: {bank.balance}")

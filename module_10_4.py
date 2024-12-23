import threading
from random import randint
from queue import Queue


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        # Гость ест от 3 до 10 секунд
        delay = randint(3, 10)
        print(f'{self.name} кушает {delay} секунд...')
        threading.Event().wait(delay)


class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()  # Очередь гостей
        self.tables = list(tables)  # Столы в кафе

    def guest_arrival(self, *guests):
        for guest in guests:
            if any(table.guest is None for table in self.tables):
                free_table = next((table for table in self.tables if table.guest is None))
                free_table.guest = guest
                print(f'{guest.name} сел(-а) за стол номер {free_table.number}')
                guest.start()
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None

            for table in self.tables:
                if table.guest is None and not self.queue.empty():
                    new_guest = self.queue.get()
                    table.guest = new_guest
                    print(f'{new_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    new_guest.start()


# Создание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]

# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)

# Приём гостей
cafe.guest_arrival(*guests)

# Обслуживание гостей
cafe.discuss_guests()

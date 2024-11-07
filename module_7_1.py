class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    __file_name = 'products.txt'

    def __init__(self):
        pass

    def get_products(self):
        """Считывает информацию о товарах из файла и возвращает все товары как строку"""
        try:
            with open(self.__file_name, 'r') as file:
                return file.read().strip()  # Возвращаем строку с товарами
        except FileNotFoundError:
            return ""  # Если файл не существует, возвращаем пустую строку

    def add(self, *products):
        """Добавляет товары в файл, если их нет в магазине"""
        existing_products = set()
        try:
            with open(self.__file_name, 'r') as file:
                # Считываем все товары из файла и сохраняем их в множество (для быстрого поиска)
                existing_products = {line.split(', ')[0] for line in file.readlines()}
        except FileNotFoundError:
            pass  # Файл может не существовать, если товаров нет

        with open(self.__file_name, 'a') as file:
            for product in products:
                # Если товар уже есть в магазине, выводим сообщение
                if product.name in existing_products:
                    print(f"Продукт {product} уже есть в магазине")
                else:
                    # Если товара нет, добавляем его в файл
                    file.write(str(product) + "\n")
                    existing_products.add(product.name)  # Добавляем продукт в множество для будущей проверки


# Пример использования классов:
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

# Первый запуск - добавляем товары в магазин
s1.add(p1, p2, p3)

# Выводим все товары, которые есть в магазине
print(s1.get_products())

# Второй запуск - пытаемся добавить повторные товары
s1.add(p1, p2, p3)

# Выводим товары из файла снова
print(s1.get_products())

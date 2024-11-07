class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        # Возвращает строковое представление товара
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        # Инкапсулированный атрибут с именем файла
        self.__file_name = 'products.txt'

    def get_products(self):
        # Считывание всех продуктов из файла
        try:
            with open(self.__file_name, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            # Если файл не существует, возвращаем пустую строку
            return ''

    def add(self, *products):
        # Считываем текущие товары в магазине
        existing_products = self.get_products().splitlines()

        for product in products:
            # Форматируем строку продукта
            product_str = str(product)

            # Проверяем, существует ли такой товар
            if product_str in existing_products:
                print(f'Продукт {product_str} уже есть в магазине')
            else:
                # Добавляем новый продукт в файл
                with open(self.__file_name, 'a', encoding='utf-8') as file:
                    file.write(product_str + '\n')
                existing_products.append(product_str)  # Обновляем список для проверки


# Пример работы программы:
s1 = Shop()

# Создаем продукты
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

# Печатаем строковое представление продукта
print(p2)  # Спагетти, 3.4, Groceries

# Добавляем продукты в магазин
s1.add(p1, p2, p3)

# Получаем все товары из магазина
print(s1.get_products())

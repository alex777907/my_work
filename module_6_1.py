# Родительский класс для животных
class Animal:
    alive = True    # Классовый атрибут, указывающий, живо ли животное
    fed = False     # Классовый атрибут, указывающий, накормлено ли животное

    def __init__(self, name):
        self.name = name           # Уникальное имя животного
        self.alive = Animal.alive  # Инициализация экземпляра атрибутом класса
        self.fed = Animal.fed      # Инициализация экземпляра атрибутом класса

    def eat(self, food):
        if not self.alive:
            print(f"{self.name} мертв и не может есть.")
            return

        if not isinstance(food, Plant):
            print(f"{self.name} может есть только растения.")
            return

        if food.edible:
            print(f"{self.name} съел {food.name}.")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}.")
            self.alive = False

# Родительский класс для растений
class Plant:
    edible = False   # Классовый атрибут, указывающий, съедобно ли растение

    def __init__(self, name):
        self.name = name          # Уникальное имя растения
        self.edible = Plant.edible # Инициализация экземпляра атрибутом класса

# Класс Mammal, наследник Animal
class Mammal(Animal):
    pass  # Наследует все атрибуты и методы от Animal

# Класс Predator, наследник Animal
class Predator(Animal):
    pass  # Наследует все атрибуты и методы от Animal

# Класс Flower, наследник Plant
class Flower(Plant):
    pass  # Растение остается несъедобным

# Класс Fruit, наследник Plant
class Fruit(Plant):
    edible = True  # Переопределяем съедобность для фруктов

    def __init__(self, name):
        super().__init__(name)      # Вызываем конструктор родительского класса
        self.edible = Fruit.edible # Устанавливаем съедобность

# Создание объектов классов
# Животные
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')

# Растения
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')


print(a1.name)    
print(p1.name)    

print(a1.alive)   
print(a2.fed)    

a1.eat(p1)       
a2.eat(p2)       

print(a1.alive)  
print(a2.fed)     

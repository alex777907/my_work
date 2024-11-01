class Animal:#класс родитель для зверушек
    alive = True
    fed = False

    def eat(self, food):
        if food.edible == True:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


class Plant:#клас родитель для растений
    edible = False

    def __init__(self, name):
        self.name = name


class Mammal(Animal):#млекопитающие-класс наследник зверушек
    def __init__(self, name):
        self.name = name


class Predator(Animal):#хищники-класс наследник зверушек
    def __init__(self, name):
        self.name = name


class Flower(Plant):#цветы-класс наследник растений
    pass


class Fruit(Plant):#фрукты-класс наследний растений
    edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
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

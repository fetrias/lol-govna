class Eda:

    def __init__(self, name, weight) -> None:
        self.name = name
        self.weight = weight

    def smert(self, p):
        print(f'О нет, меня съело {p.name}')

    def __call__(self,):
        print(f'Меня зовут {self.name} и я прибавляю свиньям {self.weight} кг')


class GuineaPig:
    
    def __init__(self, name, weight, color) -> None:
        self.name = name
        self.weight = weight
        self.color = color

    def zhrat(self, hui):
        self.weight += hui.weight
        print(f"{self.name} набрала {hui.weight} кг")
        hui.smert(self)

    def __call__(self):
        print(f'меня зовут {self.name}, я вешу {self.weight} кг и я цвета {self.color}')


p1 = GuineaPig("kartoha", 9843759384573986973587, "buff")
e1 = Eda('укроп', 7)
print(p1.weight)
p1.zhrat(e1)
print(p1.weight)
p1()
e1()
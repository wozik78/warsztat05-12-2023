# klasa ---szablon to taki minimum cech jakie musi posiadać obiekt
# pola klasy np name
# funkcje : chodzenie , gadanie , spanie

# definicja klasy

import math
class MyFirstClass:
    '''
    klasa w pythonie opisujaca punkty w przestrzeni x i y

    '''

    # metoda inicjalizujaca (konstruktor)

    def __init__(self, x=0, y=0):
        '''
        metoda inicjulizujaca

        :param x: położenie na osi x
        :param y: położenie na osi y
        '''
        # self.x = x
        # self.y = y
        self.move(x, y)
        self.reset(x, y)

    def move(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def reset(self):
        self.move(0,0)

    # funkcje magiczne , odpowidaa za sposób prezentacji obiektu
    def __repr__(self):
        return f"X={self.x}, y={self.y}"


# tworzenie obiektu klasy

p1 = MyFirstClass()
print(p1)

print(MyFirstClass.__doc__)

print(p1.__doc__)
print(p1.x)
print(p1.y)
p1.move(45, 89)
print(p1)
p1.reset()
print(p1)

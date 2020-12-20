"""
Любой экземпляр класса без переопределения метода __bool__ возвращает True.
Любое число отличное от нуля - возвращает True. 0 - возвращает False.
Строки, кортежи, списки - если они пустые, то они возвращают False. Если они что-то в себе содержат, то - True.
Чтобы экземпляр класса возвращал нам при необходимости нужное значение - нужно переопределить метод __bool__ в классе.
Если метод __bool__ не переопределен, но переопределен метод __len__,
то Python возвращает результат работы метода __len__.

"""


class Point:

    def __init__(self, coord_x1: (int, float), coord_x2: (int, float)):
        self.coord_x1 = coord_x1
        self.coord_x2 = coord_x2

    def __len__(self):  # Работает вместо функции __bool__, если она не переопределена.
        print("Call __len__")
        return abs(self.coord_x1 - self.coord_x2)

    def __bool__(self):
        print("Call __bool__")
        return self.coord_x1 != 0 or self.coord_x2 != 0  # Запомнить, что возвращает True, если выражение правда


""" 
При and - Python проверил бы первое выражение и далее не пошел бы, т.е. должны соблюстись оба условия для возвращеня True
При or - Python проверяет
"""

p1 = Point(2, 2)
p2 = Point(3, 4)
p3 = Point(0, 0)
p4 = Point(0, 4)
p5 = Point(4, 0)

print(bool(p1))
print(10 * "#")
print(bool(p2))
print(10 * "#")
print(bool(p3))
print(10 * "#")
print(bool(p4))
print(10 * "#")
print(bool(p5))

"""
Полиморфизм - возможность объектов с одинаковой спецификацией иметь различную реализацию.
Все объекты имеют один и тот же метод в классе, но вычисляется он по-разному. И теперь можно проходить по всем этим
объектам в цикле и выполнять для каждого объекта свое действие, вызывая лишь один метод.
!!!А что если метод evaluate_are оформить как property?!

"""


class Rectangle:

    def __init__(self, side_1: (int, float), side_2: (int, float)) -> None:
        self.side_1 = side_1
        self.side_2 = side_2
        super().__init__()

    def evaluate_area(self):
        return self.side_1 * self.side_2

    def __repr__(self) -> str:
        return f'Rectangle with {self.side_1} * {self.side_2} :'


class Square:

    def __init__(self, side: (int, float)) -> None:
        self.side = side
        super().__init__()

    def evaluate_area(self):
        return self.side ** 2

    def __repr__(self) -> str:
        return f'Square with {self.side} :'


class Circle:

    def __init__(self, radius: (int, float)) -> None:
        self.radius = radius
        super().__init__()

    def evaluate_area(self):
        return 3.14 * self.radius ** 2

    def __repr__(self) -> str:
        return f'Circle with {self.radius} :'


rec_1 = Rectangle(1, 2)
rec_2 = Rectangle(2, 5)
# print(rec_1.evaluate_area(), rec_2.evaluate_area())
# print(40 * "#")
sq_1 = Square(2)
sq_2 = Square(10)
# print(sq_1.evaluate_area(), sq_2.evaluate_area())
# print(40 * "#")
crl_1 = Circle(5)
crl_2 = Circle(8)
# print(rec_1.evaluate_area(), rec_2.evaluate_area())
# print(40 * "#")
figures = [rec_1, rec_1, sq_1, sq_2, crl_2, crl_1]
# А можно решить данную данную проблемы через цикл

for figure in figures:
    print(figure.__repr__(), figure.evaluate_area(), end='\n###############\n')

"""
Магические методы сравнения:
__eq__ - отвечает за ==. Equal
__ne__ - отвечает за !=.
__lt__ - отвечает за <. Less than
__le__ - отвечает за <=.
__gt__ - отвечает за >.
__ge__ - отвечает за >=.
Все методы реализовать нет необходимости. Достаточно переопределить два методы __eq__ и любое строгое сравнение.
"""


class Rectangle:

    def __init__(self, side_1: (int, float), side_2: (int, float)):
        self.side_1 = side_1
        self.side_2 = side_2

    def __eq__(self, other):
        print("__eq__")
        if isinstance(other, Rectangle):
            return self.side_1 == other.side_1 and self.side_2 == other.side_2
        else:
            raise TypeError("Need then object was type Rectangle")

    def __lt__(self, other):
        print("__lt__")
        if isinstance(other, Rectangle):
            return self.side_1 < other.side_1 and self.side_2 < other.side_2

    def __le__(self, other):
        print("__le__")
        return self == other or self < other


rec_1 = Rectangle(10, 20)
rec_2 = Rectangle(10, 20)
rec_3 = Rectangle(5, 2)
# print(rec_1 != rec_2)
# print(rec_2 != rec_1)
# print(rec_1 != rec_3)
# print(rec_3 != rec_1)
# print(40 * "#")
# print(rec_1 < rec_2)
# print(rec_2 < rec_1)
# print(rec_1 < rec_3)
# print(rec_3 < rec_1)
# print(40 * "#")
# print(rec_1 > rec_2)
# print(rec_2 > rec_1)
# print(rec_1 > rec_3)
# print(rec_3 > rec_1)
# print(40 * "#")
# print(rec_1 > rec_2)
# print(rec_2 > rec_1)
# print(rec_1 > rec_3)
# print(rec_3 > rec_1)
# print(40 * "#")
print(rec_1 >= rec_2)
print(rec_2 >= rec_1)
print(rec_1 >= rec_3)
print(rec_3 >= rec_1)
print(40 * "#")

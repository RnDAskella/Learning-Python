"""
Вычисляемые свойства.
Чтобы вычисляемое свойство постоянно не загружало процессор, необходимо,
чтобы оно сохранялось в __init__ как аттрибут и вызывалось уже оттуда.
"""


class Square:
    def __init__(self, side):
        self.__side = side
        self.__area = None
        self.__perimeter = None

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, new_side):
        self.__side = new_side
        self.__area = None
        self.__perimeter = None

    @property
    def area(self):
        if self.__area is None:
            self.__area = self.side ** 2
        return self.__area

    @property
    def perimeter(self):
        if self.__perimeter is None:
            self.__perimeter = 4 * self.__side
        return self.__perimeter


sq_1 = Square(10)
print(sq_1.area)
print(sq_1.perimeter)
sq_1.side = 20
print(sq_1.area)
print(sq_1.perimeter)

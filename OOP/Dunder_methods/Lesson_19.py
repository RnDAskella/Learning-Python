"""
Первоначально объекты сравниваются == по id (по ячейке в памяти).
Для корректного сравнения объектов необходимо переопределить метод __eq__.
Hash считается от id объекта.
Поэтому при переопределении метода __eq__ необходимо переопределить метод __hash__.
Для примера: в качестве ключей для словаря можно использовать только hashable объекты. При использовании nonehashable -
будет выдана ошибка. Поэтому если в качестве ключа хотим использовать объекты своего класса, то необходимо определить
метод __hash__.
Интересный возврат - смотри ниже.
Hash() принимает в качестве аргументов кортеж!
Увеличивающаяся переменная и обращение к ней - смотри ниже.
!!! Что проверяет is - ...
!!! Диапазон принимаемых значений hash() -
!!! Диапазон принимаемых значений id() -
"""


class Point:
    count_instance = 0

    def __init__(self, x_1: (int, float), x_2: (int, float)):
        self.x_1 = x_1
        self.x_2 = x_2
        Point.count_instance += 1
        self.count_instance = Point.count_instance  # Интересная реализация!!!

    def __eq__(self, other):
        return isinstance(other, Point) and \
               self.x_1 == other.x_1 and self.x_2 == other.x_2  # Интересный возврат!!!

    def __hash__(self):
        return hash((self.count_instance, self.x_1, self.x_2))


point_1 = Point(1, 2)
point_01 = point_1
point_2 = Point(1, 2)
point_3 = Point(2, 1)

print(f"ID point_1 = {id(point_1)},"
      f"ID point_01 = {id(point_01)},"
      f"ID point_2 = {id(point_2)}, "
      f"ID point_3 = {id(point_3)}")

print(f"ID hash_1 = {hash(point_1)},"
      f"ID hash_01 = {hash(point_01)},"
      f"ID hash_2 = {hash(point_2)}, "
      f"ID hash_3 = {hash(point_3)}")
print(point_1 == point_2)
print(point_1 == point_3)
print(point_1.count_instance)
print(point_2.count_instance)

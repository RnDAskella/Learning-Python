from math import sqrt


class Point:
    total_list_point = []

    def __init__(self, coord_x=0, coord_y=0):
        self.x = coord_x
        self.y = coord_y
        Point.total_list_point.append(self)

    def move_to(self, new_coord_x: int, new_coord_y: int):
        self.x = new_coord_x
        self.y = new_coord_y

    def evaluate_distance_between_point(self, another_point) -> float:
        if not isinstance(another_point, Point):
            raise ValueError("Argument must belong class Point")
        else:
            return sqrt((self.x - another_point.x) ** 2 + (self.y - another_point.y) ** 2)


point_1 = Point(2)
point_2 = Point(2, 4)
a = point_1.evaluate_distance_between_point(point_2)
print(a)

print(point_2 is point_1)

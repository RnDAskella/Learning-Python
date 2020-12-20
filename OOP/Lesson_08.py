"""
Моносостояние.
Меняя аттрибут у одного экземпляра - этот аттрибут меняется у всех экземпляров класса.
Добавляя новый аттрибут одному экземпляру - этот аттрибут добавляется всем экземплярам класса.
"""


class Cat:
    __shared_attr = {
        'breed': 'pers',
        'color': 'black',
    }

    def __init__(self):
        self.__dict__ = Cat.__shared_attr


cat_1 = Cat()
cat_2 = Cat()
print(cat_1.__dict__)
print(Cat.__dict__)
cat_1.age = 20
cat_1.breed = 'KING'
print(cat_1.breed)
print(cat_2.breed)

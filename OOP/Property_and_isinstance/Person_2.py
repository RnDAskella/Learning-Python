"""
Метод property().
Проверка объекта по соответствию типу isinstance().

"""
class Person:
    def __init__(self, name: str = ' ',
                 age: int = 0,
                 sex: str = ' '):
        self.name = name
        self.__age = age
        self.sex = sex

    def get_age(self):
        return self.__age

    def set_age(self, custom_age):
        if not isinstance(custom_age, (int, float)):  # Можем проходить по кортежу!!!
            raise ValueError("Custom_age must be int or float")
        self.__age = custom_age

    def delete_age(self):
        del self.__age

    age_property = property(get_age)


human_1 = Person(name='Alex', age=33, sex='M')
print(human_1.get_age())

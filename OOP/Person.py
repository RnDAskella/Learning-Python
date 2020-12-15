class Person:
    def __init__(self, name: str = ' ', age: int = 0, sex: str = ' '):
        self.name = name
        self.__age = age
        self.sex = sex

    def set_age(self, custom_age):
        if not isinstance(custom_age, (int, float)):  # Можем проходить по кортежу!!!
            raise ValueError("Custom_age must be int or float")
        self.__age = custom_age

    def get_age(self):
        return self.__age

    def delete_age(self):
        del self.__age

    person_age = property(fget=get_age, fset=set_age, fdel=delete_age)


human_1 = Person(name='Alex', age=33, sex='M')
# print(human_1.__age) # Не сможем получить доступ к приватной переменной
human_1.person_age = 100  # Установка свойства через знак присваивания
print(human_1.person_age)
del human_1.person_age
print(human_1.__dict__)
for elem in Person.__dict__:
    print(elem)

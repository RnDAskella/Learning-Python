"""
Создание геттеров, сеттеров, делитеров как свойства (декораторы).
Private and protected attributes.
"""


class Person:
    def __init__(self, name: str = ' ',
                 age: int = 0,
                 sex: str = ' '):
        self.name = name
        self.__age = age
        self.sex = sex

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, custom_age):
        if not isinstance(custom_age, int):  # Можем проходить по кортежу!!!
            raise ValueError("Custom_age must be int or float")
        self.__age = custom_age

    @age.deleter
    def age(self):
        del self.__age
        print("We deleted this attributes")

    # person_age_after_change = property(person_age_after_change)
    # person_age_after_change = person_age_after_change.getter(get_age)
    # person_age_after_change = person_age_after_change.setter(set_age)
    # person_age_after_change = person_age_after_change.deleter(delete_age)

    # person_age = property(fget=get_age,
    #                       fset=set_age,
    #                       fdel=delete_age)


def print_total_attributes(var_name: str, var_age, var_sex: str):
    human_1 = Person(name=var_name, age=var_age, sex=var_sex)
    print(human_1.__dict__)
    # print(human_1.__age) # Не сможем получить доступ к приватной переменной
    human_1.person_age = 300
    print(human_1.person_age)
    del human_1.person_age


print_total_attributes(var_name='Alex', var_age=33, var_sex='M')
h = Person()
h.age = 100
print(h.age)
del h.age
# print(h.age)

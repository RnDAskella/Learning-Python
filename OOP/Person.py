class Person:
    def __init__(self, name: str = ' ', age: int = 0, sex: str = ' '):
        self.name = name
        self.age = age
        self.sex = sex


a = Person()
print(a.age)

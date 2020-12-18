"""
Магические методы __abs__ и __len__
К строке не может быть применен метод __abs__.
К числу не может быть применен метод __len__.
Ели у экземпляра вызывать два этих метода, то они сработают некорректно,
пока их не переопределишь внутри класса.
"""


class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence

    def __len__(self):
        return len(self.sentence)

    def __abs__(self):
        return len(self)


class Snippet:
    def __init__(self, coordinate_1: (int, float), coordinate_2: (int, float)):
        self.coordinate_1 = coordinate_1
        self.coordinate_2 = coordinate_2

    def __len__(self):
        return abs(self)

    def __abs__(self):
        return abs(self.coordinate_2 - self.coordinate_1)


a = Snippet(2, 10)
b = Snippet(10, 2)
print(f"Abs where a < b : {a.__abs__()}")
print(f"Abs where b < a : {b.__abs__()}")

print(f"Abs where a < b : {a.__len__()}")
print(f"Abs where b < a : {b.__len__()}")

example = "Темный Лорд приветствует тебя!"  # Пробелы тоже считаются за символы
c = Sentence(example)

print(f"Length out example = : {c.__len__()}")
print(f"ABS out example = : {c.__abs__()}")  # пока не переопределишь этот метод в классе - будет ошибка

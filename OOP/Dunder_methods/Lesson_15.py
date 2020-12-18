"""
Dunder methods (double underscore) or magic methods.
Достатояно переопределить __repr__ и автоматически переопределится __str__.
"""


class Lion:
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):  # нужен для разработчиков
        return f"{self.name} - class Lion"

    def __str__(self):  # нужен для пользователей
        return f"This Lion - {self.name}"


leo = Lion("Simba")
print(leo)

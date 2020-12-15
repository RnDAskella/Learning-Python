class Car:
    model: str = "BMW"
    engine: float = 3.0

    def __str__(self) -> str:
        return f"This model - {self.model} and It has engine - {self.engine}"


print(getattr(Car, "engine",
              100))
"""Метод, который возвращает аттрибут класса без создания экземпляра.
Если такого аттрибута нет, то возвращает 100."""

# Car.color = "Red"  # устанавливаем новый аттрибут???
car_1 = Car()
# print(a1.color)

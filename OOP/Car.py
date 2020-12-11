class Car:
    model: str = "BMW"
    engine: float = 3.0

    def __str__(self) -> str:
        return f"This model - {self.model}"

"""
Методы __add__
Методы __mul__
Методы __sub__
Методы __truediv__
А также использование обратных магических методов.
"""


class BankAccount:
    def __init__(self, name: str, balance: (int, float)):
        self.name = name
        self.balance = balance

    def __add__(self, other):
        if isinstance(other, BankAccount):
            return self.balance + other.balance
        elif isinstance(other, (int, float)):
            return self.balance + other
        raise TypeError("For this operation needs values is int or float")

    def __radd__(self,
                 other):  # переопределение данного метода необходимо
        # для корректного вычисления суммы при смене мест слагаемых
        return self.balance + other

    def __sub__(self, other):
        if isinstance(other, BankAccount):
            return self.balance - other.balance
        elif isinstance(other, (int, float)):
            return self.balance - other
        raise TypeError("For this operation needs values is int or float")

    def __rsub__(self, other):
        return self.balance - other

    def __mul__(self, other):
        if isinstance(other, BankAccount):
            return self.balance * other.balance
        elif isinstance(other, (int, float)):
            return self.balance * other
        raise TypeError("For this operation needs values is int or float")

    def __rmul__(self, other):
        return self.balance * other

    def __truediv__(self, other):
        if isinstance(other, BankAccount):
            return self.balance / other.balance
        elif isinstance(other, (int, float)):
            return self.balance / other
        raise TypeError("For this operation needs values is int or float")

    def __rtruediv__(self, other):
        return self.balance / other


account_1 = BankAccount("Alex", 100)
account_2 = BankAccount("Kate", 500)

print(f"Результатом работы __add__ будет: {account_1 + 100}")
print(f"Результатом работы __add__ будет: {101 + account_1}")
print(f"Результатом работы __add__ будет: {account_1 + account_2}")
print(f"Результатом работы __add__ будет: {account_2 + account_1}")
print(40 * "#")
print(f"Результатом работы __sub__ будет: {account_1 - 100}")
print(f"Результатом работы __sub__ будет: {101 - account_1}")
print(f"Результатом работы __sub__ будет: {account_1 - account_2}")
print(f"Результатом работы __sub__ будет: {account_2 - account_1}")
print(40 * "#")
print(f"Результатом работы __mul__ будет: {account_1 * 100}")
print(f"Результатом работы __mul__ будет: {100 * account_1}")
print(f"Результатом работы __mul__ будет: {account_1 * account_2}")
print(f"Результатом работы __mul__ будет: {account_2 * account_1}")
print(40 * "#")
print(f"Результатом работы __truediv__ будет: {account_1 / 100}")
print(f"Результатом работы __truediv__ будет: {100 / account_1}")
print(f"Результатом работы __truediv__ будет: {account_1 / account_2}")
print(f"Результатом работы __truediv__ будет: {account_2 / account_1}")

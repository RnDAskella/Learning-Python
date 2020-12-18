"""
Пространство имен класса и экземпляра.
Важно! Необходимо отличать пространство имен класса и экземпляра.
Получить доступ к переменным класса можно: через обращение к объекту, через обращение к имени классу,
через свойство, через статичесский метод, через класс_метод.
"""


class DepartmentIT:
    PYTHON_DEV = 4
    GO_DEV = 3
    REACT_DEV = 2

    def info(self):
        print(self.PYTHON_DEV, self.GO_DEV, self.REACT_DEV)

    def info_2(self):
        print(DepartmentIT.PYTHON_DEV, DepartmentIT.GO_DEV, DepartmentIT.REACT_DEV)

    def hiring_pyt_dev_1(self):
        self.PYTHON_DEV += 1

    @classmethod
    def hiring_pyt_dev_2(cls):  # изменит переменные самого класса, не затрагивая его экземпляр
        DepartmentIT.PYTHON_DEV += 100


it_1 = DepartmentIT()
print(f"Это экземпляр до: {it_1.__dict__}")
print(f"Это класс до: {DepartmentIT.__dict__}")
# it_1.info()
it_1.hiring_pyt_dev_1()
DepartmentIT.hiring_pyt_dev_2()
print(f"Это экземпляр после: {it_1.__dict__}")
print(f"Это класс после: {DepartmentIT.__dict__}")

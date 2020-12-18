"""
Проверка в сеттере переменной по нескольким пунктам.
Проверка аттрибута через сеттер при инициализации экземпляра.
Создание и сокрытие статического метода.
"""

from string import digits


class User:
    def __init__(self, login, password_user):
        self.login = login
        self.password = password_user  # Обрати внимание, что теперь атрибут self.password - свойство

    @property
    def password(self):
        return self.__password  # А здесь продолжаем обращаться как к защищенной переменной

    @password.setter
    def password(self, password_user):
        if not isinstance(password_user, str):
            raise TypeError("Password must be string")
        if len(password_user) < 4:
            raise ValueError("Password must be more 4 symbols")
        if len(password_user) > 12:
            raise ValueError("Password must be less 12 symbols")
        if not User.__is_user_password_on_contain_digit(password_user):
            raise ValueError("Password must be at least one digit symbols")
        self.__password = password_user

    @staticmethod
    def __is_user_password_on_contain_digit(
            password):  # если таким образом защитить, то не будет видно вызова у экземпляра
        for digit in digits:
            if digit in password:
                return True
        return False


a = User('Alex', "akdjsajdaj1")

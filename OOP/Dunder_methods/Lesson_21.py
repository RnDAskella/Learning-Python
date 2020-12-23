"""
Магический метод __call__.
Экземпляр может вызываться через переменную "а()" и будет при этом выводить работу магического
метода __call__.
"""
from time import perf_counter as pc


class Counter:

    def __init__(self):
        self.counter = 0
        self.sum = 0
        self.length = 0
        print('__init__ || ', self)

    def __call__(self, *args, **kwargs):
        self.counter += 1
        self.sum = self.sum + sum(args)
        self.length += len(args)
        print(f'Our instance calls = {self.counter}')

    def evaluate_average(self):
        return self.sum / self.length


class Timer:
    def __init__(self, function):
        self.fn = function

    def __call__(self, *args, **kwargs):
        start_time = pc()
        # print(f'Вызывается функция: {self.fn.__name__}')
        result_evaluate_function = self.fn(args, kwargs)
        finish_time = pc()
        result_evaluate_timer = finish_time - start_time
        print(f'Функция работала = {result_evaluate_timer}')
        return result_evaluate_function


@Timer
def evaluate_average_value_from_list(*args):
    return args


evaluate_average_value_from_list = Timer(evaluate_average_value_from_list)(1, 2, 3)
print(evaluate_average_value_from_list)
# print(evaluate_average_value_from_list(1, 2, 3))

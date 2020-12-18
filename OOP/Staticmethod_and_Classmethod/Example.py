class Example:
    def display_hello():  # Скомпилировалось
        print("Hello")

    def display_instance_hello(self):
        print(f"Instance hello {self}")

    @staticmethod
    def static_display_hello():
        print("Static hello")

    @classmethod
    def class_display_hello(cls):
        print(f"Class hello {cls}")


def print_results_work_function_from_class_Example_01():
    object_01 = Example()
    Example.display_hello()
    # object_01.display_hello()  # не сработает


def print_results_work_function_from_class_Example_02():
    object_01 = Example()
    # Example.display_instance_hello()  # не сработает, так как нужна передача объекта как аргумента
    object_01.display_instance_hello()


def print_results_work_function_from_class_Example_03():
    object_01 = Example()
    Example.static_display_hello()
    object_01.static_display_hello()  # не сработает


def print_results_work_function_from_class_Example_04():
    object_01 = Example()
    Example.class_display_hello()
    object_01.class_display_hello()


print_results_work_function_from_class_Example_01()
print_results_work_function_from_class_Example_02()
print_results_work_function_from_class_Example_03()
print_results_work_function_from_class_Example_04()

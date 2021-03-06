from abc import *


class NothingTodo:
    pass  # If nothing exists on class


class Complex:
    a = 1

    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    # no parameter function
    def a(self):
        pass

    def ab(self, text):
        pass

    @property
    def get_model(self):
        """without get_model(), able to use `get_model`"""
        return self.a

    # private
    def _ab(self):
        pass


def run_complex():
    x = Complex(3.0, -4.5)
    x.r, x.i, x.a  # (3.0, -4.5, 1)
    print(x.get_model)


# Inheritance
class Inheritance(Exception):
    pass


# Multiple inheritance
class MultipleInheritance(Complex, Inheritance):
    pass


class _PrivateClass:  # private class
    pass


john = _PrivateClass()  # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000

print(john.__dict__)  # {'name': 'John Doe', 'dept': 'computer lab', 'salary': 1000}
print(john.__class__)  # <class '__main__.Employee'>
print(john.__dir__())  # <class '__main__.Employee'>. same with dir(john)


class AbstractClass(metaclass=ABCMeta):
    @abstractmethod
    def drive(self):
        pass


class ImplmentedClass(AbstractClass):
    def drive(self):
        print("k5 drive")


def run_abstract():
    ImplmentedClass().drive()


class Reverse:
    """Iterator for looping over a sequence backwards."""

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


def run_iteration():
    """custom iteration"""
    rev = Reverse('spam')
    for char in rev:  # for..in use this : it = iter(rev); next(it); next(it); ...
        print(char)


class MasicMethod:
    def __getattribute__(self, item):
        print(item, "객체에 접근하셨습니다.")

    def __call__(self, *args, **kwargs):
        print("호출됨")

    def __str__(self):
        return "this is string object"


def run_masic_method():
    m = MasicMethod()
    m()  # call __call__
    m.data  # call __getattribute__
    print(m)  # call __str__

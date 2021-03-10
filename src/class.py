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

    # private
    def _ab(self):
        pass


x = Complex(3.0, -4.5)
x.r, x.i, x.a  # (3.0, -4.5, 1)


# Inheritance
class CustomException(Exception):
    pass

# Multiple inheritance
class A(Complex, CustomException):
    pass

class _Employee: # private class
    pass

john = _Employee()  # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000

print(john.__dict__)  # {'name': 'John Doe', 'dept': 'computer lab', 'salary': 1000}
print(john.__class__)  # <class '__main__.Employee'>
print(john.__dir__())  # <class '__main__.Employee'>. same with dir(john)


# custom iteration

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


rev = Reverse('spam')
for char in rev: # for..in use this : it = iter(rev); next(it); next(it); ...
    print(char)
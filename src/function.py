def printme(text):
    """This prints a passed string into this function"""
    print(text)
    return
printme("dd")
printme(text="My string")

def printInfo(name, age=35):
    """This prints a passed info into this function"""
    print("Name: ", name)
    print("Age ", age)
    return


def printInfo2(arg1, *vartuple):
    """This prints a variable passed arguments"""
    print("Output is: ")
    print(arg1)

    for var in vartuple:
        print(var)
    return
printInfo2(70, 60, 50)

def initlog(*args):
    """Define function later with"""
    pass  # TODO : Remember to implement this!


# function can be set on other variable
a = initlog
a("1")

# Warning :: The default value is evaluated only once. This makes a difference when the default is a mutable object such as a list
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))


# [1]
# [1, 2]
# [1, 2, 3]

# If you don't want to share mutable list. use this way.
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


# position only, /, both, *, keyword only
def pos_only_arg(arg, /):
    print(arg)
def kwd_only_arg(*, arg):
    print(arg)
def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)


pos_only_arg(1)
kwd_only_arg(arg=3)
combined_example(1, standard=2, kwd_only=3)

# keworded variable '**'
def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))

greet_me(name="yasoob")
greet_me(**{"name":"yasoob"})
# name = yasoob
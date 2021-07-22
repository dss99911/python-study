def print_me(text):
    """This prints a passed string into this function"""
    print(text)
    return


print_me("dd")
print_me(text="My string")


def print_info(name, age=35):
    """This prints a passed info into this function"""
    print("Name: ", name)
    print("Age ", age)
    return


def with_type_str(name: str):
    print(name)


def with_type_dict(name: dict):
    print(name)


def print_info2(arg1, *vartuple):
    """This prints a variable passed arguments"""
    print("Output is: ")
    print(arg1)

    for var in vartuple:
        print(var)
    return


print_info2(70, 60, 50)


def var_args(*args):
    """Define function later with"""
    pass  # TODO : Remember to implement this!


# function can be set on other variable
a = var_args
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
greet_me(**{"name": "yasoob"})


# name = yasoob

# %%
def tuple_return():
    return 1, 2, 3
    # return (1, 2, 3)


a1, a2, a3 = tuple_return()


#%%

def return_type_define()-> dict:
    return {}



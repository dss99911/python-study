# assigning
import numbers

counter = 100  # An integer assignment
miles = 1000.0  # A floating point
name = "John"  # A string

# multiple assignment
a = b = c = 1
a2, b2, c2 = 1, 2, "john"

a = None  # null

# delete variable
del a, b, c


# Global & Local variables
def sum2(arg1, arg2):
    total = arg1 + arg2  # Here total is local variable.
    return total


total2 = 0  # This is global variable.

# Refer Global variable
Money = 2000


def accessGlobalVariable():
    global Money
    Money = Money + 1


# show global or local variables
globals()
locals()
#%%
import numbers
# 변수가 class인지 체크
print(isinstance(int, type))
print(issubclass(int, numbers.Number))
#%%

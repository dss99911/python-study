from functools import reduce

lis = [1, 3, 5, 6, 2, ]

# using reduce to compute sum of list
print("The sum of the list elements is : ", end="")
print(reduce(lambda a, b: a+b, lis))
#%%
# reduce with initial value


def add(d, i):
    d.append(i)
    return d
print(reduce(lambda d, i : add(d, i), lis, []))

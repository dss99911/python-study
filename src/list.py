squares = [1, 4, 9, 16, 25]

print(1 in squares)
print(1 not in squares)
print(squares + [36, 49, 64, 81, 100])  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Modify list
squares[1] = 5
squares.append(5)
squares[2:3] = [1, 2, 3, 4]  # Change 2-3 with the list
squares[:] = []  # clear

# tuple : similar with list but read-only
tuple = 'abcd', 786, 2.23, 'john', 70.2
tinytuple = (123, 'john')
x, y, _, _, z = tuple # ignore some value
a, *_, b = tuple # ignore some value

print(tuple)  # Prints complete list
print(tuple[0])  # Prints first element of the list
print(tuple[1:3])  # Prints elements starting from 2nd till 3rd
print(tuple[2:])  # Prints elements starting from 3rd element
print(tinytuple * 2)  # Prints list two times
print(tuple + tinytuple)  # Prints concatenated lists

# ('abcd', 786, 2.23, 'john', 70.200000000000003)
# abcd
# (786, 2.23)
# (2.23, 'john', 70.200000000000003)
# (123, 'john', 123, 'john')
# ('abcd', 786, 2.23, 'john', 70.200000000000003, 123, 'john')

# Join List with separator
",".join(map(lambda x: str(x), tuple))

from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.pop()
queue.popleft()

print([x ** 2 for x in range(10)])
print(list(map(lambda x: x ** 2, range(10))))
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print([[row[i] for row in matrix] for i in range(4)])
# transposed [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

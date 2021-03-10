# Lambda
sum = lambda arg1, arg2: arg1 + arg2
sum(1, 2)


def make_incrementor(n):
    return lambda x: x + n


f = make_incrementor(42)
f(0)  # 42
f(1)  # 43

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
# [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

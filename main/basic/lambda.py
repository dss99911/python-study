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

# Partial
# 부분함수. 특정 파라미터를 미리 설정하여, 함수를 생성
from functools import partial
def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)
square(2) == 4
cube(2) == 8

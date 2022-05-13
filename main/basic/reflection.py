import inspect

def a(p1: str, p2):
    pass

## argument확인
print(inspect.signature(a).parameters)

## 함수 이름
a.__name__


class A:
    def ab(self):
        print("ab called")
getattr(A(), "ab")()
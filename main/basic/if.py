# if statement block is deviced by indent after ':'
a = 10
b = True
if a > 100 > 200:
    print("Value of expression is 100")
    print(a)
elif b:
    pass
elif not b:
    pass
elif a == 200:
    print("c")
    if a == 300:
        print("d")
    else:
        print("e")
else:
    print("b")


# ternary operator
def ternary_operator():
    return "success" if (b) else "fail"

def get_or():
    a = [1]
    print(a or 2)  # [1]
    a = []
    print(a or 2)  # 2
    a = None
    print(a or 2)  # 2
    a = 0
    print(a or 2)  # 2


if __name__ == '__main__':
    print(ternary_operator())

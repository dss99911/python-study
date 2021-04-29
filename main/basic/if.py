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

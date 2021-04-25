def num_gen():
    for i in range(3):
        yield i

g = num_gen()

for i in g:
    print(i)
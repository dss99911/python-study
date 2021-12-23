# For in
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))


# For with index
#%%
def for_index():
    a = ['Mary', 'had', 'a', 'little', 'lamb']
    for i in range(len(a)):
        print(i, a[i])
    print(i)

#%%

def for_index_enumerate():
    for i, v in enumerate(['tic', 'tac', 'toe']):
        print(i, v)
    # 0 tic
    # 1 tac
    # 2 toe


# Ignore value
for _ in range(10):
    print("1")

# break and else(else is invoked when 'for' statement isn't broken.
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n // x)
            break
        if True:  # just show continue
            continue
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

# While
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a + b

# pass do nothing. if there is nothing to do on block. use 'pass' not to do anything
while True:
    pass  # Busy-wait for keyboard interrupt (Ctrl+C)

#%% # for to array
arr = [f"test{i}" for i in [1, 2]]
arrIf = [f"test{i}" for i in [1, 2] if i > 1]

#%% for two array by zip
a = [1,2,3]
b = [1,2,3]

for c, d in zip(a,b):
    print(c,d)
# https://docs.python.org/3/tutorial/modules.html

import moduleFibo
from moduleFibo import fib, fib2
from moduleFibo import *  # import all
import moduleFibo as f
from moduleFibo import fib as fibonacci
import sample.fibo as f2 # when importing from different directory. need as

moduleFibo.fib(1)
fib(1)
f.fib(1)
fibonacci(1)
f2.fib(1)
# If module.py is imported by other, then this is not invoked.
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))

# shows member field or functions of the imported module
dir(moduleFibo)


# https://docs.python.org/3/tutorial/modules.html


from fibo import fib, fib2
from fibo import *  # import all
import fibo as f
from fibo import fib as fibonacci
import directory.moduleChild as f2  # when importing from different directory. need as
from directory.moduleChild import *  # when importing from different directory. need as

# need to configure parent package. https://stackoverflow.com/questions/11536764/how-to-fix-attempted-relative-import-in-non-package-even-with-init-py/27876800#27876800
from ..moduleParent import *

fibParent(1)
fib(1)
f.fib(1)
fibonacci(1)
f2.fibChild(1)
# If module.py is imported by other, then this is not invoked.
if __name__ == "__main__":
    import sys

    fib(int(sys.argv[1]))

# shows member field or functions of the imported module
dir(f2)

# https://docs.python.org/3/tutorial/errors.html

try:
    fh = open("testfile", "w")
    fh.write("This is my test file for exception handling!!")
except IOError as err:
    print(f"Error: can\'t find file or read data {err}")
except(AssertionError, TypeError):
    print("handle multiple error")
except Exception as e:
    print(f"any Exception : {e}")
    raise ValueError("some error") from e  # exception chaining
    # raise  # raise same error again after printing
except :
    print(f"any Exception 2nd way without parameter")
else:
    print("Written content in the file successfully")
    fh.close()
finally:
    print("any case")

raise ValueError("error")


# create custom exception
class CustomException(Exception):
    pass


#%%

from contextlib import suppress
import os
with suppress(FileNotFoundError):
    os.remove("sadf")
    print("apple") # this is not called
print("bear")

#%%

import traceback

def bb():
    raise ValueError

try:
    bb()
except ValueError:
    tb = traceback.print_exc(file=sys.stdout)
    tb = traceback.format_exc()
else:
    tb = "No error"
finally:
    print(tb)
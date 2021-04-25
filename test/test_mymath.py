from main.testcode.mymath import *

# call `pytest`, `pytest -v` on shell

def test_average():
    assert average([1, 2, 3]) == 2

def test_average():
    assert wrong_average([1, 2, 3]) == 2
from main.testcode.mymath import *

# call `pytest`, `pytest -v` on shell

def test_average():
    assert average([1, 2, 3]) == 2

def test_average():
    assert wrong_average([1, 2, 3]) == 2


# Mock https://docs.python.org/ko/3/library/unittest.mock-examples.html
from unittest.mock import MagicMock, call

print = MagicMock(name='buy_market_order')

print.return_value = "ddf"

a = print(3, 4, 5, key='value') # return "ddf"
print.assert_called_with(3, 4, 5, key='value')
a = print(4, 4, 5, key='value') # return "ddf"
print.assert_has_calls([call(3, 4, 5, key='value'), call(4, 4, 5, key='value')])

#%%

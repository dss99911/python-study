#%%
from typing import Optional
from typing import Union

a = {}
is_dict = type(a) == dict

optional: Optional[str] = None

b: Union[bool, int] = 1  # avaialble int or bool
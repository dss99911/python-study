import importlib

var_name = importlib.import_module("time")
print(var_name.time())
#%%
import sys
sys.path.insert(0, 'main/modules/external/ex_code.zip')
import ex_code

#%%

import importlib

importlib.reload(aa)
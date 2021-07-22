dict_ = {} # underscore at last is convention
dict_['one'] = "This is one"
dict_[2] = "This is two"
dict2 = {'one': "This is one", 2: "This is two"}
a = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])  # make dict

print(dict_.keys())  # Prints all the keys
print(dict_.values())  # Prints all the values

list(dict_)  # ['one', 2]

def copy_dict():
    dict_.copy()
    dict(dict_)

def merge_dict():
    dict1 = {"a":1}
    dict2 = {"b":2}
    dict3 = dict1 | dict2 # pyton 3.9
    dict3 = {**dict1, **dict2}

#get or None
if dict_.get('ddd') is None:
    print("dddd")


def delete_dict_item():
    del dict['one']  # remove entry with key 'one'
    dict.clear()  # remove all entries in dict
    del dict

# iterate by key
for key in dict_:
    print(key)

# iterate by (key,value)
for key, value in dict_.items():
    print(key, value)


#%%
dict_

def print_cache_multiple_creation():

    multiple_creation = list(filter(lambda t: (t[1] != "") ,dict_.items()))
    if len(multiple_creation) > 0:
        print("[Cache Multiple Creation]")
        for k in multiple_creation:
            print(k)
print_cache_multiple_creation()

#%%

{x: x**2 for x in (2, 4, 6)} # {2: 4, 4: 16, 6: 36}

# Zip
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))


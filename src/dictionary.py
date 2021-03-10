dict_ = {} # underscore at last is convention
dict_['one'] = "This is one"
dict_[2] = "This is two"
dict2 = {'one': "This is one", 2: "This is two"}
a = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])  # make dict

print(dict_.keys())  # Prints all the keys
print(dict_.values())  # Prints all the values

list(dict_)  # ['one', 2]

# del dict['one']  # remove entry with key 'one'
# dict.clear()  # remove all entries in dict
# del dict

# iterate by key
for key in dict_:
    print(key)

# iterate by (key,value)
for key, value in dict_.items():
    print(key, value)


{x: x**2 for x in (2, 4, 6)} # {2: 4, 4: 16, 6: 36}

# Zip
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
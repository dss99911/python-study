basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
a = set('abracadabra')  # {'a', 'r', 'b', 'c', 'd'}.
b = set('alacazam')
a - b  # {'r', 'd', 'b'}
a | b  # {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
a & b  # {'a', 'c'}
a ^ b  # {'r', 'd', 'b', 'm', 'z', 'l'}

a = {x for x in 'abracadabra' if x not in 'abc'}  # {'r', 'd'}
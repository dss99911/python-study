from time import sleep
from pprint import pprint
from colorama import Back, Fore, Style

# pretty print
pprint({"obj" : 1})

# print on shell with color
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('Finished')
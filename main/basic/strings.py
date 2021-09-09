import re
from datetime import datetime

#%%

def strips():
    print("/sdf/".rstrip("/"))
    print("/sdf/".lstrip("/"))
    print("/sdf/".strip("/"))
    print(" adsf ".strip())

strips()
#%%

def split():
    a = "abc def\nadsf"
    a = a.split()  # split any whitespace
    print(a)
    a = "abc,def,adsf"
    a = a.split(",")
    print(a)

#%%
def replace():
    a = "abc 123".replace("1", "2")
    print(a)
    a = re.sub(r'\d', '', a)
    print(a)

replace()
#%%
def float_or_none(text: str):
    try:
        return float(text)
    except ValueError:
        return None


def formatting():
    print('What is your {0}?  It is {1}.'.format("name", "hyun"))
    print(format(float("2.25e-05"), 'f'))
    print('log/{}{:%Y-%m-%d}.log'.format("dd", datetime.now()))
    a = 1123.232323
    print(f"{a:.2f}") # 소수점 2번째까지만 출력

def startsWith(text: str):
    return text.startswith("aa")

def contains():
    return 'substring' in "any_string substring substring"

#%%

from difflib import SequenceMatcher
def text_diff():
    s = SequenceMatcher(lambda x: x == " ",
                        "ABCDE",
                        "ABEDE")
    print(s.ratio())
text_diff()
#%%

# print new line
print('C:\some\name')

# raw (print '\n')
print(r'C:\some\name')

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# convert to bytes
b"ddd"

# unicode
u"asdf"

print(3 * 'un' + 'ium')  # unununium

print('Py' 'thon')  # Python (automatically concatenated)
print('A'  # AB
      'B')

prefix = 'Py'
print(prefix + 'thon')  # Concatenate variable and string literal
#%%
word = 'Python'
print(word[0])  # 'P'
print(word[-1])  # last character
print(word[0:2])  # characters from position 0 (included) to 2 (excluded)
print(word[:2] + word[2:])  # Python

len(word)  # size of word
print(word[0:-1])
#%%
# Formatting https://docs.python.org/3/tutorial/inputoutput.html
'What is your {0}?  It is {1}.'.format("name", "kim")
'What is your {}?  It is {}.'.format("name", "kim")
year = 2020
event = "corona"
print(f'Results of the {year} {event}')
print('event is %s' % event)

string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
string1 or string2 or string3  # 'Trondheim'

print(repr("hello\n"))  # "'hello\n'", representation. the string interpretor understand

### Methods
message = "dsfsd  "
message = message.lower()
message = message.strip()

if __name__ == '__main__':
    replace()

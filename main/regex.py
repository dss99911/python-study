import re
re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')  # ['foot', 'fell', 'fastest']

# replace all
re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')  # 'cat in the hat'

# trim
"  asdf   ".strip()


#%%
import re
st = '123 124123@ybl'
m = re.match(r"(?i)q\d+@",st) # 처음부터 매칭되어야 함.
regex = ["\\b123\\b", "123"]

result = []
for r in regex:
    result.append(re.search(r,st))


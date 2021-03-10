import json

obj = [1, 'simple', 'list']
json.dumps(obj) # '[1, "simple", "list"]'

f = open('workfile', 'w')
json.dump(obj, f)  # save json to file
x = json.load(f)  # load json from file
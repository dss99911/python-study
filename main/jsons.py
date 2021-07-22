import json

def make_json_string():
    obj = [1, 'simple', 'list']
    json.dumps(obj) # '[1, "simple", "list"]'

def save_json_to_file():
    obj = [1, 'simple', 'list']
    f = open('workfile', 'w')
    json.dump(obj, f)  # save json to file

def load_json_from_file():
    f = open('workfile', 'r')
    x = json.load(f)  # load json from file o


def json_obj_from_string():
    json_string = '''
    {
      "students": [
        {
          "name": "Millie Brown",
          "active": true,
          "rollno": 11
        },
        {
          "name": "Sadie Sink",
          "active": true,
          "rollno": 10
        }
      ]
    }
    '''
    print(json.loads(json_string))
#%%
json_obj_from_string()
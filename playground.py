import json

def to_json(dict):
    return json.dumps(dict)

def from_json(dict):
    my_str = json.loads(dict)
    return my_str


my_dict = dict()

my_dict = {"abf":1, "SDgs":2342, "3g35g":2342}


print(to_json(my_dict))

print(from_json(my_dict))





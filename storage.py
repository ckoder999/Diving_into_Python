import os
import tempfile
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--key", action="store")
parser.add_argument("--value", action="store")

args = parser.parse_args()

key_value = dict()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

if args.value:
    key_value[args.key] = args.value
#print(key_value)


#if not(value):
#пишем json
    with open(storage_path, 'a') as write_file:
        json.dump(key_value, write_file)
else:
#читаем json
#You should pass the file contents (i.e. a string) to json.loads(), not the file object itself
    with open(storage_path) as read_file:
        data = json.loads(read_file.read())


#print(data)
    #json.loads(read_file)
    #data1 =   json.JSONDecoder().decode({"key": "value"})


#else:
#    print("Adding new entry")

#with open(storage_path, 'a') as f:
#    json.dumps(key_value, f)
    #json.dumps(value, f)

"""
key_value = dict
key_value = {1 : 'bac'}

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

with open(storage_path, 'w') as f:
    json.dump(key_value, f)
    #json.load(f)
"""

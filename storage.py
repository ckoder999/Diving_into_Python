import os
import tempfile
import json

key_value = dict
key_value = {1 : 'bac'}

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
print(storage_path)

def add_value(key)

with open(storage_path, 'w') as f:
    json.dump(key_value, f)


    #json.load(f)



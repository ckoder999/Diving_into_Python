import os
import tempfile
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--key", action="store")
parser.add_argument("--value", action="store")

args = parser.parse_args()
#key = args.key
#value = args.value
my_dict = dict()
my_dict[args.key] = args.value

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

if args.value:

#пишем json

    with open(storage_path, 'a') as write_file:
        json.dump(my_dict, write_file)
        write_file.write("\n")

else:
#читаем json
#You should pass the file contents (i.e. a string) to json.loads(), not the file object itself
    with open(storage_path, 'r') as read_file:
        my_list = list()
        for line in read_file:
            #line = read_file.readline()
            data = json.loads(line)
            if args.key in data.keys():
                my_list.append(data[args.key])

    if not my_list:
        print(" ")
    else:
        #for p in my_list:
        print(*my_list, sep=', ')




#print(data)
    #json.loads(read_file)
    #data1 =   json.JSONDecoder().decode({"key": "value"})






"""
key_value = dict
key_value = {1 : 'bac'}

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

with open(storage_path, 'w') as f:
    json.dump(key_value, f)
    #json.load(f)
"""

import functools
import json

def to_json(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        #в эталонном решении поставили вспомогательную переменную result
        #result = func(*args, **kwargs)
        #return json.dumps(result)

        json_result = json.dumps(func(*args, **kwargs))
        return json_result
    return wrapper

@to_json
def get_data():
    return {
        'data': 42
    }

print(get_data())



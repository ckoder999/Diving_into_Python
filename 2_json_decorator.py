"""Чтобы передавать данные между функциями, модулями или разными системами
 используются форматы данных. Одним из самых популярных форматов является JSON.
 Напишите декоратор to_json, который можно применить к различным функциям,
 чтобы преобразовывать их возвращаемое значение в JSON-формат.
 Не забудьте про сохранение корректного имени декорируемой функции."""


import functools
import json

def to_json(func):
    @functools.wraps(func) # сделать, чтобы передавалось название функции?
    def wrapper(*args, **kwargs):
        json_result = json.dumps(func(*args, **kwargs))
        return json_result
    return wrapper

import random

my_dict = {}
my_dict = dict.fromkeys(['a','b','c'],[1,2,3])
print(my_dict)


@to_json
def get_data(foo):
    return foo


print(get_data(my_dict))  # вернёт '{"data": 42}'

# TypeError: the JSON object must be str, bytes or bytearray, not 'dict'
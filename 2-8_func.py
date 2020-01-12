#1
from datetime import datetime

def get_time():
    """Get seconds now"""
    return datetime.now()

get_time()

#2
def string_split(tag_string):
    tag_split = list()

    for tag in tag_string.split(","):
        tag_split.append(tag)
    return tag_split


string_split("python, mooc, coursera")

#3
def add(x: int, y: int) -> int:
    return x + y

print(add(3, 2))
print(add('still', ' works'))

#4
def extender(source_list, extend_list):
    source_list.extend(extend_list)

a_list = [1, 2, 3]
b_list = [4, 5, 6]

extender(a_list, b_list)

print(a_list)

#5
def replacer(source_tuple, replace_tuple):
    source_tuple = replace_tuple

a_tuple = ('1', '2', '3')
b_tuple = ('9', '8', '7')

replacer(a_tuple, b_tuple)

print(a_tuple)

#6
def say(greeting, name):
    print(f"{greeting} {name}!")

say('Hello', 'Kitty')
say(name = 'Kitty', greeting='Hello')

#7
number = 0

def change():
    number += 1
    return number

#change()

#8
# аргумент по умолчанию

def greeting(name='it\'s me'):
    print(f"Hello {name}")

greeting()
greeting('Mike')

#9
def append_1(iterable=[]):
    iterable.append(1)
    return iterable

#print(append_1([1]))

print(append_1())
print(append_1())

print(append_1.__defaults__)

#print(append_1())
#если дефолтные значения являются изменяемыми, в них можно записывать, и их значение изменяется!
#чтобы этого избежать, нужно определять дефолтные значения как None

def function(iterable=None):
    if iterable is None:
        iterable = []
#или

def function (iterable=None):
    iterable = iterable or []
#то есть, если параметр не передан, создаем новый список "на лету"




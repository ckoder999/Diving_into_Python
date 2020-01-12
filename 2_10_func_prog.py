# функция, которая создает другую функцию
def get_multiplier():
    def inner(a, b):
        return a * b
    return inner


mul = get_multiplier()
print(mul(3, 10))

#теперь это  inner!
print(mul.__name__)

# замыкание - функция inner использует переменную из области видимости функции get_multiplier_num
def get_multiplier_num(number):
    def inner(a):
        return a * number
    return inner

mul1 = get_multiplier_num(3)
print(mul1(15))

#map
def squarify(a):
    return a*a

#map возвращает объект типа map, по которому можно итерироваться
#приводим его к list
print(list(map(squarify, range(5))))
#на чистом python:
square_list = list()
for num in range(5):
    square_list.append(squarify(num))
print(square_list)

#filter позволяет проитерировать объект, отфильтровав его значения
def is_pos(a):
    return a > 0

print(list(filter(is_pos, range(-2,4))))
#filter работает так:
ispos_list = []
for num in range(-2,4):
    if is_pos(num):
        ispos_list.append(num)
print(ispos_list)

#lambda или анонимные функции

print(list(map(lambda x: x ** 2, range(5))))
#лямбда - это анонимная функция: класс function
print(type(lambda x: x ** 2))

print(list(filter(lambda x: x > 0, range(-2,4))))

#Напишите функцию, которая превращает список чисел в список строк.
#мой вариант
num_list = [1, 4, 315, -10, 77]

print(list(map(lambda x: str(x), num_list)))

print(type(num_list[1]))
#без лямбды
num_str = []

for a in num_list:
    num_str.append(str(a))

print(num_str)
#как должно быть
def stringify(num_list):
    return list(map(str, num_list))

print(stringify((num_list)))









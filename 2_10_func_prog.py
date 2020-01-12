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

print(list(map(squarify, range(5))))

print(map(squarify, range(5)))

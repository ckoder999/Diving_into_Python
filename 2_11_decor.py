# написать декоратор, который записывает в лог результат декорируемой функции
import functools

def logger(func):  # определили наш декоратор
    @functools.wraps(func) # wraps подменяет аргументы, docstrings и названия
    # в данном случае summator.__name__ останется summator, а не wrapped
    def wrapped(num_list):  # заменим наш summator на wrapped num_list
        result = func(num_list)  # результат выполнения функции
        with open('log.txt', 'w') as f:
            f.write(str(result))  # пишем его в лог-файл
        return result

    return wrapped  # вернём его, перезаписав summator


@logger  # применяем декоратор - результат выполнения summator должен записываться в лог-файл
def summator(num_list):
    return sum(num_list)

# применяя декоратор, мы подменяем фунцию сумматор новой фунцией wrapped
# она будет выполняться, принимая num_list, получает результат работы сумматора, записывает его в файл и возвращает себя

# запись в файл, название которого передается

def logger(filename):
    def decorator(func):
        def wrapped(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filename, 'w') as f:
                f.write(str(result))
            return result
        return wrapped
    return decorator


@logger('/Users/eugene/Desktop/COURSERA/Diving_into_Python/log.txt')
def summator(num_list):
    return sum(num_list)


summator([1,24,6,67, 8])


#decorator chaining

def first_decorator(func):
    def wrapped1():
        print("Inside first_decorator product")
        print(func.__name__)
        return func()
    return wrapped1


def second_decorator(func):
    def wrapped2():
        print("Inside second_decorator product")
        print(func.__name__)
        return func()
    return wrapped2

@first_decorator
@second_decorator
def decorated():
    print("Finally called:...")

decorated()

# decorated = first_decorator(second_decorator(decorated))

print(decorated.__name__)

#
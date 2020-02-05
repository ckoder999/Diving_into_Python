import sys
def process_file(file):
    num = count_rows(file)
    print(f"Rows count: {num}")


def count_rows(file):
    count = 0
    with open(file) as f:
        for _ in f:
            count +=1
        return count

def _main():
 #  process_file(sys.argv[1])
    pass


if __name__ == "__main__":
    _main()


while True:
    try:
        s = input("Enter a number ")
        b = int(s)
        break
   # except: нужно указать явно, какой тип исключения мы обрабатываем, чтобы не перехватывать все исключения
   # (например, KeyboardInterrupt, возникающий при нажатии Crtl+C
    except ValueError:
        print("Incorrect value")
    #else: #этот блок вызывается в случае, если никакого исключения не произошло
    #    break
    except KeyboardInterrupt: #обработчик для KeyboardInterrupt
        print("The program stopped")
        break

#обработка нескольких исключений

big_number = 100_000
while True:
    try:
        num = input("Enter a number")
        int_num = int(num)
        big_number = big_number / int_num
        break
    except (ZeroDivisionError, ValueError): # если для некоторых исключений обработчик выглядит одинаково,
                                            # передаем их в список исключений
        print("Error!")

# иерархия exception'ов
# +--LookupError
#     +--IndexError
#     +--KeyError

print(issubclass(IndexError, LookupError))
print(issubclass(KeyError, LookupError))

# можем обработать несколько исключений при помощи родительского класса

database = {
    "green": ["onions", "W", "kalabash"],
    "red": ["flag", "blood", "90s"]
}

try:
    color = input("Enter a color")
    number = input("Enter a number")
    label = database[color][int(number)]
    print(f"You have chosen {label}")

# except IndexError, KeyError
except LookupError:
    print("Object not found")


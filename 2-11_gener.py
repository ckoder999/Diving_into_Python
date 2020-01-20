def even_range(start, end):
    current = start
    while current < end:
        yield current
        current += 2


for number in even_range(0, 5):
    print(number)

b = even_range(0, 5)
print(next(b))
print(next(b))
print(next(b))
print(next(b))



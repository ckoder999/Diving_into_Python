import random

numbers = []

for _ in range(10):

    numbers.append(random.randint(1, 20))

print(numbers)
print(sorted(numbers, reverse=True))

numbers.sort(reverse=False)
#print(list(reversed(numbers)))

num2 = numbers.copy()
print(num2)


print(numbers.count(10))

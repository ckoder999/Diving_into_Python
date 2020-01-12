import random

random_set = set()

while True:
    number = random.randint(1, 10)
    if number in random_set:
        break

    random_set.add(number)

print(len(random_set) + 1)
import random

numbers = []
k = random.randint(5, 15)

for _ in range(k):
    numbers.append(random.randint(1, 30))

numbers.sort()
print(numbers)


half_size = len(numbers) // 2
mediane = None

if k % 2 == 1:
    mediane = numbers[half_size]
else:
    mediane = sum(numbers[half_size - 1:half_size + 1]) / 2

print(mediane)

import statistics

print(statistics.median(numbers))



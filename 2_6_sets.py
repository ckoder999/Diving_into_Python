odd_set = set()
even_set = set()

for i in range(10):
    if i % 2:
        odd_set.add(i)
    else: even_set.add(i)

print(odd_set)
print(even_set)

union_set = odd_set | even_set
print(union_set)

intersect_set = odd_set.intersection(even_set)
print(intersect_set)

symm_diff = odd_set ^ even_set
print(symm_diff)

frozen = frozenset('Karl', 'Filip' , 'Zacher')

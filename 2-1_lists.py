
collections = ['tuple', 'list', 'dict', 'set']

for idx, collection in enumerate(collections):
    print("# {} {}".format(idx, collection))

#enumerate возвращает индекс и текущий элемент коллекции

collections.append('ordered dict')

collections.extend(['hash table', 'map'])


none_list = [None] * 10
#
collections.append([2342.2 , False])

print(collections)

print(collections[:] is collections)

collections += [None]
print(collections)

del(collections[-1])

coll2 = []
print(coll2)

for i in range(10):
    coll2.append(str(i))
print("".join(coll2))
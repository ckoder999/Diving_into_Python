import this

zen = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

zen_map = dict()

for word in zen.split(): # делит строку с указанным разделителем и помещает элементы в list
    zen_word_clear = word.strip(',.-!').lower()# strip возвращает копию строки, в которой убирает пробелы (если нет
                                            # аргументов) или указанные символы ( если нужно убрать запятую,
                                            # используем replace(',', '')
    if zen_word_clear not in zen_map:
        zen_map[zen_word_clear] = 0

    zen_map[zen_word_clear] += 1

print(zen_map) # это словарь
zen_items = zen_map.items() # это список, состоящий из таплов
# items возвращает новый вид объектов списка в виде объекта view object
#  они позволяют динамически видеть изменения нашего списка
print(zen_items)

import operator

word_count_items = sorted(zen_items, key=operator.itemgetter(1), reverse = True)
# возвращает новый отсортированный список
# sorted(iterable, *, key=None, reverse=False)

print(word_count_items[:3])

#Решение через Counter

from collections import Counter # Counter предназначен для подсчета объектов
                                # это коллекция, где элементы - ключи, а их количество - значения
                                #It's a dict subclass for counting hashable objects

cleaned_list = []

for word in zen.split():
    cleaned_list.append(word.strip(',.-!').lower())

print(Counter(cleaned_list).most_common(3))
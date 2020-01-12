with open('/Users/Eugene/file.txt') as f:
#устарело
#f = open('/Users/Eugene/file.txt', 'r')

#f.write("Coursera Python\nBlood, sweat and tears\n")

#читаем файл построчно
    print(f.readline())

#читаем из файла содержимое, записываем в список каждую строку отдельно
    print(f.readlines())

#показываем указатель - где мы находимся в файле
    print(f.tell())

#ставим указатель на начало
    f.seek(0)

#не нужно
#f.close()


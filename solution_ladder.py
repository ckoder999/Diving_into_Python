import sys
row_num = int(sys.argv[1])
for i in range(row_num):
    str = ""
    for j in range(row_num - i - 1):
        str +=' '
    for j in range(i + 1):
        str +='#'
    print(str)


import sys

num_steps = int(sys.argv[1])

for i in range(num_steps):
    print(" " * (num_steps - i - 1), "#" * (i + 1), sep="")

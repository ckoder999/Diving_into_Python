import sys
row_num = int(sys.argv[1])
print(type(row_num))
for i in range(row_num):
    for j in range(row_num - i - 1):
        print(" ", end="")
    for j in range(i + 1):
        print("#", end="")
    print("\n")

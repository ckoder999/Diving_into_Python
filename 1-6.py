import sys, math

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

D = b * b - 4 * a * c
if D ==0 :
    print("No answer")
    exit()
if D>0:
    print(int((-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)))
    print(int((-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)))
elif D<0:
    print(int(-b / (2 * a)))
    print(int(-b / (2 * a)))




import sys
import math

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

d = b * b - 4 * a * c

x1 = (-b + math.sqrt(d)) / (2 * a)
x2 = (-b - math.sqrt(d)) / (2 * a)

print(int(x1))
print(int(x2))
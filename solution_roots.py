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

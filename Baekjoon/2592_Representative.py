import sys

Sum = 0
Arr = list()

for _ in range(10):
    Temp = int(sys.stdin.readline().rstrip())
    Arr.append(Temp)
    Sum += Temp

print("%d" % (Sum / 10))


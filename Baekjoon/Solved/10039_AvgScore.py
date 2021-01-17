import sys

Sum = 0
for I in range(5):
    Input = int(sys.stdin.readline().rstrip())
    if Input < 40:
        Sum += 40
    else:
        Sum += Input
print("%d" % (Sum / 5))

import time
import sys

A = []
B = []
Sum = 0.0


for _ in range(10):
    T = time.process_time()
    input()
    A.append(time.process_time() - T)

for _ in range(10):
    T = time.process_time()
    sys.stdin.readline()
    B.append(time.process_time() - T)

for I in range(10):
    print("%.10f" % (A[I]))
    Sum += A[I]
print("평균 : %.10f" % (Sum / 10))

Sum = 0
for I in range(10):
    print("%.10f" % (B[I]))
    Sum += B[I]
print("평균 : %.10f" % (Sum / 10))

import sys

N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    A, B = [int(Num) for Num in sys.stdin.readline().rstrip().split()]
    print(A + B)

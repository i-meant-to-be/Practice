import sys

N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    A, B = [int(Num) for Num in sys.stdin.readline().rstrip().split()]
    One = [(A ** I) % 10 for I in [4, 1, 2, 3]]
    for I in range(4):
        if One[I] == 0:
            One[I] = 10
    print(One[B % 4])

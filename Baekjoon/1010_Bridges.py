import sys
from itertools import combinations

N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    west, east = [int(num) for num in sys.stdin.readline().rstrip().split()]
    for I in range(1, west + 1):
        print(len(list(combinations((east - I) * [None], 3))))

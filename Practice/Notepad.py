from sys import stdin
from itertools import combinations

input = stdin.readline
num, target = [int(_) for _ in input().split()]
cards = [int(_) for _ in input().split()]
print(max(sum(case) for case in combinations(cards, 3) if sum(case) <= target))

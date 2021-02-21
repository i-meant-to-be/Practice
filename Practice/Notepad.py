"""
5
4 1 5 2 3
5
1 3 7 9 5
"""
from sys import stdin

input = stdin.readline
target_nums = list()
source_nums = list()
input()
target_nums.extend([int(num) for num in input().split()])
input()
source_nums.extend([int(num) for num in input().split()])
print(source_nums, target_nums)
for num in source_nums:
    print(1 if target_nums.count(num) else 0)

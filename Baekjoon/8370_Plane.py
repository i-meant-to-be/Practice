from sys import stdin

input = stdin.readline

A, B, C, D = [int(num) for num in input().rstrip().split()]
print("%d" % (A * B + C * D))

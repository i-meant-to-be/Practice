from sys import stdin

input = stdin.readline

n, m = [int(num) for num in input().rstrip().split()]
print("%d\n%d" % (n // m, n % m))

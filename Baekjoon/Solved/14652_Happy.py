import sys


N, M, K = [int(num) for num in sys.stdin.readline().rstrip().split()]
print(K // M, K % M)

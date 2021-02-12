from sys import stdin

arr = [int(stdin.readline()) % 42 for num in range(10)]
print(len(set(arr)))

from sys import stdin

input = stdin.readline
num = int(input().rstrip())
for _ in range(num):
    rpt, string = input().rstrip().split()
    for char in string:
        print(f"{char * int(rpt)}", end="")
    print()

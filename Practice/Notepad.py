from sys import stdin

input = stdin.readline

string = input().strip()
if len(string) == 0:
    count = 0
else:
    count = string.count(" ") + 1
print(f"{count}")

import sys

string = sys.stdin.readline().rstrip()
for I in range(26):
    print(string.index(chr(97 + I)) if string.count(chr(97 + I)) else -1, end=' ')
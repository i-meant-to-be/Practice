from sys import stdin

input = stdin.readline

sentence = input().rstrip()
alphabet = ["c=", "c-", "d-", "lj", "nj", "s=", "z="]
count = 0
pointer = 0

while pointer != len(sentence):
    if sentence[pointer:pointer + 3] == "dz=":
        pointer = pointer + 3
    elif alphabet.count(sentence[pointer:pointer + 2]):
        pointer = pointer + 2
    else:
        pointer = pointer + 1
    count += 1

print(count)

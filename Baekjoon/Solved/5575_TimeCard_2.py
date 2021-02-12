from sys import stdin

input = stdin.readline

out = list()
for i in range(3):
    a, b, c, d, e, f = [int(num) for num in input().rstrip().split()]
    total_sec = d*3600 + e*60 + f - a*3600 - b*60 - c
    out.append(total_sec // 60 // 60)
    out.append(total_sec // 60 % 60)
    out.append(total_sec % 60)
print(f"{out[0]} {out[1]} {out[2]}")
print(f"{out[3]} {out[4]} {out[5]}")
print(f"{out[6]} {out[7]} {out[8]}")

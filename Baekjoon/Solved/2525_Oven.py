'''
if B + C <= 59:
    print("%d %d" % (A, B + C))
elif B + C == 60 and A <= 22:
    print("%d %d" % (A + 1, 0))
elif B + C >= 60 and A <= 22:
    print("%d %d" % (A + Count, B + C - 60 * Count))
elif B + C >= 60 and A == 23:
    print("%d %d" % (B + C - 60 * Count))
'''

A, B = [int(Num) for Num in input().split(' ')]
C = int(input())
Count = (B + C) / 60

if Count + A >= 24:
    Hr = (A + Count) % 24
else:
    Hr = A + Count

if B + C >= 60:
    Min = (B + C) % 60
else:
    Min = B + C

print("%d %d" % (Hr, Min))

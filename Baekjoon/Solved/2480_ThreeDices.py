A, B, C = [int(Num) for Num in input().split(' ')]

if (A == B == C):
    print(10000 + 1000 * A)
elif (A == B or A == C):
    print(1000 + 100 * A)
elif (B == C):
    print(1000 + 100 * B)
else:
    print(100 * max(A, B, C))

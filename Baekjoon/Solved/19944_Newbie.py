N, M = [int(Num) for Num in input().split(' ')]

if M == 1 or M == 2:
    print("NEWBIE!")
elif 3 <= M <= N:
    print("OLDBIE!")
else:
    print("TLE!")

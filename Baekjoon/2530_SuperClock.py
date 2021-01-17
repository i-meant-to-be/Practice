import math

Start = [int(Num) for Num in input().split(' ')]
Time = int(input())

End = [0, 0, Time % 60]
Carry = [math.floor(Time / 3600)]
Carry.append(math.floor((Time - Carry[0] * 3600) / 60))

if Start[0] + Carry[0] >= 24:
    End[0] = (Start[0] + Carry[0]) % 24
else:
    End[0] = Start[0] + Carry[0]

if Start[1] + Carry[1] >= 60:
    End[1] = (Start[1] + Carry[1]) % 24
else:
    End[1] = Start[1] + Carry[1]

print("%d %d %d" % (End[0], End[1], End[2]))

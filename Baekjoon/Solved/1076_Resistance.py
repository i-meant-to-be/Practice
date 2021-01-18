import sys

Resist = list()
Color = ("black", "brown", "red",
         "orange", "yellow", "green",
         "blue", "violet", "grey", "white")

for I in range(3):
    Resist.append(Color.index(sys.stdin.readline().rstrip()))
print((Resist[0] * 10 + Resist[1]) * (10 ** Resist[2]))

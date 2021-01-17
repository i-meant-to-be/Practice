A = int(input())
Temp = input()
B = [int(Char) for Char in list(Temp)]

for Num in [A * B[2], A * B[1], A * B[0], A * int(Temp)]:
    print(Num)

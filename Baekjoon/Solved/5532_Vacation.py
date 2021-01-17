import math

Input = []
for I in range(5):
    Input.append(int(input()))

if Input[1] % Input[3] != 0:
    Korean = int(math.floor(Input[1] / Input[3])) + 1
else:
    Korean = Input[1] / Input[3]

if Input[2] % Input[4] != 0:
    Math = int(math.floor(Input[2] / Input[4])) + 1
else:
    Math = Input[2] / Input[4]

print("%d" % (Input[0] - (Math if Math >= Korean else Korean)))

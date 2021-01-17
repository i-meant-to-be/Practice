'''
import math

Input = input().split(' ')
Input = [int(Num) for Num in Input]

X = math.sqrt(Input[0] ** 2 / (Input[1] ** 2 + Input[2] ** 2))
Height = math.floor(X * Input[1])
Width = math.floor(X * Input[2])

print(Height, Width)
'''

import math

Input = [int(Num) for Num in input().split(' ')]
X = math.sqrt(Input[0] ** 2 / (Input[1] ** 2 + Input[2] ** 2))
print(math.floor(Input[1] * X), math.floor(Input[2] * X))

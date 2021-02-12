from sys import stdin
from typing import List

input = stdin.readline


def time_subtraction(arr: List) -> List:
    carry = 0

    if arr[5] - arr[2] < 0:
        work_s = 60 - abs(arr[5] - arr[2])
        carry = -1
    else:
        work_s = arr[5] - arr[2]
        carry = 0

    if arr[4] - arr[1] + carry < 0:
        work_m = 60 - abs(arr[4] - arr[1]) + carry
        carry = -1
    else:
        work_m = arr[4] - arr[1] + carry
        carry = 0

    work_h = arr[3] - arr[0] + carry

    return [work_h, work_m, work_s]


A = time_subtraction([int(num) for num in input().rstrip().split()])
B = time_subtraction([int(num) for num in input().rstrip().split()])
C = time_subtraction([int(num) for num in input().rstrip().split()])

print(f"{A[0]} {A[1]} {A[2]}")
print(f"{B[0]} {B[1]} {B[2]}")
print(f"{C[0]} {C[1]} {C[2]}")

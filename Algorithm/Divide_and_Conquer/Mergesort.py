from typing import List
from math import floor


def merge(front_half, rear_half, left_arr, right_arr, arr):
    """ indexed from 0 """
    i, j, k = 0, 0, 0
    temp_arr = list()

    while i < front_half and j < rear_half:
        if left_arr[i] < right_arr[j]:
            temp_arr.append(left_arr[i])
            i += 1
        else:
            temp_arr.append(right_arr[j])
            j += 1
        k += 1
    if i == front_half:
        temp_arr.extend(right_arr[j:])
    else:
        temp_arr.extend(left_arr[i:])
    arr.clear()
    arr.extend(temp_arr)


def mergesort(arr: List) -> None:
    if len(arr) > 1:
        left_arr = list()
        right_arr = list()
        front_half = int(floor(len(arr) / 2))
        rear_half = len(arr) - front_half
        left_arr.extend(arr[:front_half])
        right_arr.extend(arr[front_half:])
        mergesort(left_arr)
        mergesort(right_arr)
        merge(front_half, rear_half, right_arr, left_arr, arr)


if __name__ == "__main__":
    A = [27, 10, 12, 20, 25, 13, 15, 22]
    print(A)
    mergesort(A)
    print(A)

""" mergesort 함수 하나로 정리하기
merge를 mergesort 안에 포함시키기 """

from typing import List
from math import floor


def mergesort(array: List) -> None:

    if len(array) > 1:
        left_array = list()
        right_array = list()
        mid = int(floor(len(array) / 2))

        left_array.extend(array[:mid])
        right_array.extend(array[mid:])
        print(left_array, right_array)
        assert array == left_array + right_array
        mergesort(left_array)
        mergesort(right_array)
        __merge(left_array, right_array, array)


def __merge(left_array: List, right_array: List, array: List) -> None:
    left_index = 1
    right_index = 1
    upper_index = 1

    while left_index < len(left_array) and right_index < len(right_array):
        if left_array[left_index] < right_array[right_index]:
            array[upper_index] = left_array[left_index]
            left_index += 1
        else:
            array[upper_index] = right_array[right_index]
            right_index += 1
        upper_index += 1

    if len(left_array) > len(right_array):
        array[upper_index:] = left_array[left_index:]
    else:
        array[upper_index:] = right_array[right_index:]


"""
인덱스가 아직 산만함. 정리 필요.
i, j, k, h, m 등의 변수들이 무엇을 의미하는지 확실한 이해 필요.
"""

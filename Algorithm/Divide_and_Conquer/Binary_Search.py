from math import floor
from typing import List


def binary_search(array: List, key: int) -> int:
    size_of_array = len(array)

    def __recursion(low: int, high: int) -> int:
        mid = int(floor((low + high) / 2))

        if low > high:
            return 0
        else:
            if array[mid] == key:
                return mid
            elif array[mid] < key:
                __recursion(low, mid - 1)
            else:
                __recursion(mid + 1, high)

    return __recursion(0, size_of_array)

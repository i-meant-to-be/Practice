import sys
import time
from typing import List


# 1st solution: Brute force
def brute_force(nums: List[int], target: int) -> List[int]:
    for I in range(len(nums)):
        for J in range(I + 1, len(nums)):
            if target == nums[I] + nums[J]:
                return I, J


# 2nd solution: used 'in' operation
def in_operation(nums: List[int], target: int) -> List[int]:
    for I, J in enumerate(nums):
        subtract = target - J
        if subtract in nums[I + 1:]:
            return I, nums[I + 1:].index(subtract) + (I + 1)


# Input arguments
nums = [int(num) for num in sys.stdin.readline().rstrip().split()]
target = int(sys.stdin.readline().rstrip())

start_time = time.process_time()
answer = brute_force(nums, target)
elapsed_time = time.process_time() - start_time
print(answer, "%.0f elapsed." % (elapsed_time * 1000))

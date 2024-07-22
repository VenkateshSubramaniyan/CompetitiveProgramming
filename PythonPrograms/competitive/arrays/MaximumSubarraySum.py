from typing import List

import sys


def maxSubArray(nums: List[int]) -> int:
    currSum = 0
    maxSum = -sys.maxsize - 1

    for i in nums:
        currSum += i
        if (maxSum < currSum):
            maxSum = currSum
        if (currSum < 0):
            currSum = 0
    return maxSum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(nums))

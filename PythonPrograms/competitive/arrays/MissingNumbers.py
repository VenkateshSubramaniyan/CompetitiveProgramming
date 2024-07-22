from typing import List


def missingNumber(arr: List[int]):
    total = 0
    for i in range(len(arr)):
        total += i - arr[i]

    return total


nums = [3, 0, 1]
# nums = [9,6,4,2,3,5,7,0,1]

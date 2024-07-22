from typing import List
import heapq


def longestConsecutive(nums: List[int]) -> int:
    # initializing list
    nums = (5, 7, 9, 10, 1, 3)
    if (len(nums) == 0):
        return 0
    hash = set()
    totalmax = 0

    for i in nums:
        hash.add(i)
    for i in hash:
        if i - 1 not in hash:
            cur = i
            count = 1

            while cur + 1 in hash:
                cur += 1
                count += 1
            totalmax = max(totalmax, count)
    return totalmax


print(longestConsecutive([5, 7, 9, 1, 3]))

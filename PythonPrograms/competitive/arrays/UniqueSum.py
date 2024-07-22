from typing import List


def sumOfUnique(nums: List[int]) -> int:
    count_map = dict()
    total = 0
    for i in nums:
        count_map[i] = count_map.get(i, 0) + 1
    for key, value in count_map.items():
        if value == 1:
            total += key
    return total


nums = [1, 2, 3, 2]
print(sumOfUnique(nums))

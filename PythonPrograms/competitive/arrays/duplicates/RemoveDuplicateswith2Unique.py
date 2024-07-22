from typing import List


def removeDuplicates(nums: List[int]) -> int:
    i = 0
    count = 0
    ptr = 0
    if len(nums) < 2:
        return len(nums)
    while i < len(nums):
        if i == len(nums) - 1:
            count += 1
            return count
        elif nums[i] != nums[i + 1]:
            nums[ptr] = nums[i]
            count += 1
            i += 1
            ptr += 1
        else:
            temp = nums[i]
            nums[ptr] = nums[i]
            nums[ptr + 1] = nums[i + 1]
            ptr += 2
            count += 2
            while (i < len(nums) and nums[i] == temp):
                i += 1

    print(nums)
    return count


nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]

# nums=[1,1,1,2,2,3]
# nums=
print(removeDuplicates(nums))

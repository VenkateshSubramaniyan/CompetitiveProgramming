from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        end = len(nums) - 1
        start = 0
        while (start <= end):
            mid = (start + end) // 2
            if (nums[mid] < target):
                start = mid + 1
            elif (nums[mid] > target):
                end = mid - 1
            else:
                return mid
        return start


nums = [1, 3, 5, 6]
target = 8
soln = Solution()
print(soln.searchInsert(nums, target))

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited = set()
        for i in nums:
            if visited.__contains__(i):
                return True
            else:
                visited.add(i)
        return False


soln = Solution()
print(soln.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))

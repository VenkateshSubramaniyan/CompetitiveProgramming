class Solution:
    def singleNumber(self, nums: []) -> int:
        res=0
        for i in nums:
            res=res^i
        return res



res=Solution().singleNumber(nums=[1,3,5,4,3,1])
print(res, end=" ")
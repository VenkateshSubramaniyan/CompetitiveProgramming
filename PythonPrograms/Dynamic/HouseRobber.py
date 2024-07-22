from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(self.robit(nums),self.robit(nums[::-1]))

    def robit(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        dp=[0]*n
        dp[0]=nums[0]
        dp[1]=max(dp[0],nums[1])
        for i in range (2,n-1):
            dp[i]=max(dp[i-2]+nums[i],dp[i-1])
        return dp[n-2]

nums = [2,3,2]
res=Solution().rob(nums)
print(res)
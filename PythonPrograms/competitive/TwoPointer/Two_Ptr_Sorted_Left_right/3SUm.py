from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    pairs = []
    nums.sort()
    print(nums)

    for i, n in enumerate(nums):
        # Skip positive integers
        if n > 0:
            break

        if i > 0 and n == nums[i - 1]:
            continue

        left=i+1
        right=len(nums)-1

        # print(i, n)
        while left<right:
            sum=n+nums[left]+nums[right]
            if sum>0:
                right-=1
            elif sum<0:
                left+=1
            else:
                pairs.append([n,nums[right],nums[left]])
                right-=1
                left+=1
                while nums[left] == nums[left - 1] and left < right: # Duplicate avoidance
                    left += 1

    return pairs


nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))

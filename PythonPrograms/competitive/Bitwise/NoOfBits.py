def hammingWeight(n: int) -> int:
    res = 0
    while n > 0:
        res += n % 2
        n = n >> 1
    return res

print(hammingWeight(5))

# https://leetcode.com/problems/number-of-1-bits/
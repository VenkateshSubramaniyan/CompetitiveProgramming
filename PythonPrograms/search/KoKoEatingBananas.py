import math
from typing import List


def minEatingSpeed(self, piles: List[int], h: int) -> int:
    l, r = 1, max(piles)
    result = r
    while l <= r:
        k = (l + r) // 2
        hours = 0
        for p in piles:
            hours += math.ceil(p / k)
        if (hours <= h):
            r = k - 1
            result = min(result, k)
        else:
            l = k + 1
    return result

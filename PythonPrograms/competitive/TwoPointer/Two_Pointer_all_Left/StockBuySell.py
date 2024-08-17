from typing import List


def stoclBuySell(prices: List[int]) -> int:
    maxProfit = 0
    leftPtr = 0
    if (len(prices) < 2):
        return maxProfit
    rightPtr = 1
    while (rightPtr < len(prices) - 1):
        if prices[leftPtr] < prices[rightPtr]:
            maxProfit = max(maxProfit, prices[rightPtr] - prices[leftPtr])
        else:
            leftPtr += 1
        rightPtr += 1
    return maxProfit


prices = [7, 1, 5, 3, 6, 4]
print(stoclBuySell(prices))

from typing import List


def maxProfit(prices: List[int]) -> int:
    left = 0
    right = 1
    profit = 0
    while right < len(prices):
        current_profit = prices[right] - prices[left]
        if prices[left] < prices[right]:
            profit = max(current_profit , profit)
        else:
            left = right
        right += 1
    return profit

print(maxProfit([2,4,1]))



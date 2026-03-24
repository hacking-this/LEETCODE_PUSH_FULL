1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        left = 0
4        max_profit = 0
5        right = 1
6        for right in range(len(prices)):
7            profit= prices[right]-prices[left]
8            if profit>=0:
9                max_profit = max(profit,max_profit)
10            else:
11                left=right
12        return max_profit
13            
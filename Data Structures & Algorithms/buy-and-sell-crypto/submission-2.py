class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)):
            if i == 0: minLeft = prices[i]
            profit = prices[i] - minLeft
            if profit > res: res = profit
            if prices[i] < minLeft:
                minLeft = prices[i]
        return res
    


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Sliding Windows (2 pointers move toward same direction)
        l, r = 0, 1
        maxP = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else: 
                l = r   # Found a new minimum price. Reset buy day.
            r += 1
        return maxP
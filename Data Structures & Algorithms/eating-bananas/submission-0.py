from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l < r:
            mid = l + (r - l)//2
            time = 0
            for i in range(len(piles)):
                time += ceil(piles[i]/mid)
            
            if time <= h:
                r = mid
            else:
                l = mid + 1
        return l
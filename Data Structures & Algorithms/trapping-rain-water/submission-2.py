class Solution:
    def trap(self, height: List[int]) -> int:
        #Two Pointers
        res = 0
        l, r = 0, len(height) - 1
        maxLeft =  height[0]
        maxRight = height[r]
        
        while l < r:           
            if maxLeft > maxRight:
                r -= 1
                res += max(0, min(maxLeft, maxRight) - height[r])
                maxRight = max(maxRight, height[r])
                
            else:
                l += 1
                res += max(0, min(maxLeft, maxRight) - height[l])
                maxLeft = max(maxLeft, height[l])            
        return res
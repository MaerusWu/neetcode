class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        maxLength = 0
        l = 0
        
        # Standard Sliding Window Loop
        for r in range(len(s)):
            # 1. Shrink Phase: If duplicate, remove from left until valid
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            # 2. Expansion Phase: Add the new character
            seen.add(s[r])
            
            # 3. Calculation Phase: NOW the window is valid. Calculate length.
            # (r - l + 1) is the current clean window size.
            maxLength = max(maxLength, r - l + 1)
            
        return maxLength
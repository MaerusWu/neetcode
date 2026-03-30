class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding Windows
        seen = set()
        maxLength = 0
        if len(s) == 0: return 0
        if len(s) == 1: return 1

        l, r = 0, 1
        seen.add(s[l])

        while r < len(s):
            while s[r] in seen:                        
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            length = r - l + 1
            maxLength = max(maxLength, length)    
            r += 1
        return maxLength
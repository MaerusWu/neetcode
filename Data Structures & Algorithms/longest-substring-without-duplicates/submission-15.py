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
            length = r - l + 1
            if s[r] in seen:                        
                l += 1
                r = l + 1
                seen.clear()
                seen.add(s[l])
                length -= 1
            else:
                seen.add(s[r])
                r += 1
            print(length)
            print(seen)
            maxLength = max(maxLength, length)     
        return maxLength
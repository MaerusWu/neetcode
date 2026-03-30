class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Strategy: Sliding Window + Set
        # Time: O(N), Space: O(min(N, A))
        
        seen = set()
        l = 0
        max_len = 0
        
        for r in range(len(s)):
            # If current char is a duplicate, shrink window from the left
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            # Now the window is valid, add the new char
            seen.add(s[r])
            
            # Update max length
            max_len = max(max_len, r - l + 1)
            
        return max_len
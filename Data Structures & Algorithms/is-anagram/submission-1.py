class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashTable  = [0]*26
        for i in range(len(s)):
            hashTable[ord(s[i]) - ord('a')] += 1
            hashTable[ord(t[i]) - ord('a')] -= 1
        for count in hashTable:
            if count != 0:
                return False
        return True         
            

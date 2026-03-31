class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        count1 = [0] * 26
        count2 = [0] * 26
        match = 0

        for i in range(len(s1)):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1

        for i in range(26):
            if count1[i] == count2[i]:
                match += 1
        
        for i in range(len(s1), len(s2)):

            if match == 26: return True

            index = ord(s2[i]) - ord('a')
            count2[index] += 1
            if count1[index] == count2[index] : match += 1
            if count1[index] +1 ==  count2[index]: match -=1

            index = ord(s2[i - len(s1)]) - ord('a')
            count2[index] -= 1
            if count1[index] == count2[index] : match += 1
            if count1[index] -1 ==  count2[index]: match -=1

        return match == 26

             
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        for i in numSet:
            if not i-1 in numSet:
                length = 1
                while i + length in numSet:
                    length += 1
                res = max(res, length)
        return res

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))
        prefix = 1
        suffix = 1
        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]

            res[len(nums) - i - 1] *=suffix 
            suffix  *= nums[len(nums) - i -1]
        return res
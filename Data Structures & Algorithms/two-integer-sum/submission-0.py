class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for index in range(len(nums)):
            if target - nums[index] in dict:
                return [dict[target - nums[index]],index]
            else:
                 dict[nums[index]] = index

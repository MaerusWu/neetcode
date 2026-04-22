class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        if len(nums) == 0: return -1
        while l < r:
            mid = l + (r - l)//2
            if nums[mid] == target:
                return mid
            #Left portion
            if nums[mid] >= nums[l]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid
            
            #right portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid
                else:
                    l = mid + 1

        if nums[l] == target:
            return l
        else: return -1    
        
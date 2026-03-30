class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer, Integer> result = new HashMap<Integer, Integer>();
        for(int i=0; i<nums.length; i++){
            if(result.containsKey(nums[i])){
                return true;
            } else{
                result.put(nums[i], nums[i]);
            }
        }
        return false;
    }
}
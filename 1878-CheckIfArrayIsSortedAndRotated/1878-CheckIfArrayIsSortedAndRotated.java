// Last updated: 8/13/2025, 8:17:06 PM
class Solution {
    public boolean check(int[] nums) {
        int count = 0;
        for(int i=0;i<nums.length;i++){
            int prev = (i+nums.length-1)%nums.length;
            if(nums[prev]>nums[i]){
                count++;
            }
        }
        if(count<=1){
            return true;
        }
        return false;
    }
}
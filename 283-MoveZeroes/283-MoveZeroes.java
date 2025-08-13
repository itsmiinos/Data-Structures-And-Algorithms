// Last updated: 8/13/2025, 8:20:36 PM
class Solution {
    public void moveZeroes(int[] nums) {
        int i = 0;
        for(int j=0;j<nums.length;j++){
            if(nums[j]!=0){
                int temp = nums[j];
                nums[j] = nums[i];
                nums[i] = temp;
                i++;
            }
        }
    }
}
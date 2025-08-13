// Last updated: 8/13/2025, 8:15:35 PM
class Solution {
    public boolean canSortArray(int[] nums) {
        int n = nums.length;
        for(int i=0;i<n-1;i++){
            if(nums[i]>=nums[i+1]){
                if(Integer.bitCount(nums[i])==Integer.bitCount(nums[i+1])){
                    int temp = nums[i];
                    nums[i] = nums[i+1];
                    nums[i+1] = temp;
                }
                else{
                    return false;
                }
            }
        }

        for(int i=n-1;i>0;i--){
            if(nums[i]<=nums[i-1]){
                if(Integer.bitCount(nums[i])==Integer.bitCount(nums[i-1])){
                    int temp = nums[i];
                    nums[i] = nums[i-1];
                    nums[i-1] = temp;
                }
                else{
                    return false;
                }
            }
        }
        return true;
    }
}
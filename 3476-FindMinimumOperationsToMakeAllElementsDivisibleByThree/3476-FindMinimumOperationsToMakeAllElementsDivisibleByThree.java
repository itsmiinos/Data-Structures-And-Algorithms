// Last updated: 8/13/2025, 8:15:13 PM
class Solution {
    public int minimumOperations(int[] nums) {
        int n = nums.length;
        int count = 0;

        for(int i=0;i<n;i++){
            if(nums[i]%3!=0){
                count++;
            }
        }

        return count;
    }
}
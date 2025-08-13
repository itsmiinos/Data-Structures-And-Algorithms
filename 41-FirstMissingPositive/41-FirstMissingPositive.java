// Last updated: 8/13/2025, 8:23:58 PM
class Solution {
    public int firstMissingPositive(int[] nums) {
        int n = nums.length;
        int i=0;
        while(i<n){
            if(nums[i] == i+1){
                i++;
                continue;
            }

            if(nums[i] <= 0 || nums[i] > n){
                i++;
                continue;
            }

            else{
                int idx = nums[i]-1;
                if(nums[idx] == nums[i]){
                    i++;
                }
                else{
                    int temp = nums[idx];
                    nums[idx] = nums[i];
                    nums[i] = temp;
                }
            }
        }

        for(int j=0;j<n;j++){
            if(j!=nums[j]-1){
                return j+1;
            }
        }
        return n+1;
    }
}
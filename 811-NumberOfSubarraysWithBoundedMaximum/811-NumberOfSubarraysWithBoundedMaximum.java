// Last updated: 8/13/2025, 8:18:55 PM
class Solution {
    public int numSubarrayBoundedMax(int[] nums, int left, int right) {
        int n = nums.length;
        int lgei = 0;
        int validStartingPoints = 0;
        int ans = 0;
        for(int i=0;i<n;i++){
            if(nums[i]>right){
                lgei = i+1;
                validStartingPoints = 0;
            }
            else if(nums[i]<=right && nums[i]>=left){
                validStartingPoints = i-lgei+1;
                ans = ans+validStartingPoints;
            }
            else{
                ans = ans+validStartingPoints;
            }
        }

        return ans;
    }
}
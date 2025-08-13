// Last updated: 8/13/2025, 8:17:27 PM
class Solution {
    public int[] runningSum(int[] nums) {
        int n = nums.length;
        int[]p = new int[n];
        p[0] = nums[0];
        for(int i=1;i<n;i++){
            p[i] = p[i-1] + nums[i];
        }
        return p;
    }
}
// Last updated: 8/13/2025, 8:20:48 PM
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] p = new int[n];
        p[0] = nums[0];
        for(int i=1;i<n;i++){
            p[i] = p[i-1] * nums[i];
        }
        int suffix = 1;
        for(int i=n-1;i>0;i--){
            p[i] = p[i-1] * suffix;
            suffix = suffix * nums[i];
        }
        p[0] = suffix;
        return p;
    }
}
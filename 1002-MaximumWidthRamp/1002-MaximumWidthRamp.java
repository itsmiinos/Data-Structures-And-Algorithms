// Last updated: 8/13/2025, 8:18:08 PM
class Solution {
    public int maxWidthRamp(int[] nums) {
        int n = nums.length;
        int[] max_right = new int[n];
        max_right[n-1] = nums[n-1];
        
        for(int i=n-2;i>=0;i--){
            max_right[i] = Math.max(nums[i],max_right[i+1]);
        }

        int result = 0;
        int l = 0;
        for(int r=0;r<n;r++){
            while(nums[l] > max_right[r]){
                l++;
            }
            result = Math.max(result , r - l);
        }
        return result;
    }
}
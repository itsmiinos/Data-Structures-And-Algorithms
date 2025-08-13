// Last updated: 8/13/2025, 8:15:16 PM
class Solution {
    public boolean isArraySpecial(int[] nums) {
        int n = nums.length;
        for(int i=0;i<n-1;i++){
            boolean flag1 = nums[i]%2==0;
            boolean flag2 = nums[i+1]%2==0;
            if(flag1^flag2==false)return false;
        }
        return true;
    }
}
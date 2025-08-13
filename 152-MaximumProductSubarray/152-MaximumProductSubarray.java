// Last updated: 8/13/2025, 8:21:50 PM
class Solution {
    public int maxProduct(int[] nums) {
        int n = nums.length;
        int p1 = 1;
        int maxP1 = Integer.MIN_VALUE;
        int p2 = 1;
        int maxP2 = Integer.MIN_VALUE;

        for(int i=0;i<n;i++){
            if(p1==0){
                p1 = nums[i];
            }
            else{
                p1 = p1*nums[i];
            }
            maxP1 = Math.max(p1,maxP1);
        }

        for(int i=n-1;i>=0;i--){
            if(p2==0){
                p2 = nums[i];
            }
            else{
                p2 = p2*nums[i];
            }
            maxP2 = Math.max(p2,maxP2);
        }

        return Math.max(maxP1,maxP2);
    }
}
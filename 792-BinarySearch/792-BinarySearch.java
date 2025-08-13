// Last updated: 8/13/2025, 8:18:58 PM
class Solution {
    public int search(int[] nums, int target) {
        int lo = 0;
        int hi = nums.length-1;
        int mi = lo + (hi-lo)/2;
        while(lo<=hi){
            if(nums[mi]==target){
                return mi;
            }
            else if(nums[mi]>target){
                hi = mi-1;
                mi = lo + (hi-lo)/2;
            }
            else{
                lo = mi+1;
                mi = lo + (hi-lo)/2;
            }
        }
        return -1;
    }
}
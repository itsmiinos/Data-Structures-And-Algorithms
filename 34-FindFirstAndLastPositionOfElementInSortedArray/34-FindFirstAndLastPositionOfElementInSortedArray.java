// Last updated: 8/13/2025, 8:24:08 PM
class Solution {
    public int[] searchRange(int[] nums, int target) {
        int l = lowerBound(nums,target);
        int u = upperBound(nums,target);

        if(l==nums.length || nums[l]!=target){
            return new int[] {-1,-1};
        }
        else{
            return new int[] {l,u-1};
        }
    }

    public int upperBound(int []nums , int target){
        int low = 0 ;
        int high = nums.length-1;
        int ans = nums.length;
        while(low<=high){
            int mid = low + (high-low)/2;

            if(nums[mid]>target){
                ans = mid;
                high = mid - 1;
            }
            else{
                low = mid + 1;
            }
        }
        return ans;
    }

    public int lowerBound(int[] nums , int target){
        int low = 0;
        int high = nums.length -1;
        int ans = nums.length;
        while(low<=high){
            int mid = low + (high - low)/2;
            
            if(nums[mid]>=target){
                ans = mid;
                high = mid - 1;
            }
            else{
                low = mid + 1;
            }
        }
        return ans;
    }
}
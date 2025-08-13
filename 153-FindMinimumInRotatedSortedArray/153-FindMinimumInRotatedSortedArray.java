// Last updated: 8/13/2025, 8:21:56 PM
class Solution {
    public int findMin(int[] nums) {
        int start = 0;
        int n = nums.length;
        int end = n-1;

        if(n == 1){
            return nums[0];
        }

        while(start<=end){
            int mid = start + (end-start)/2;
            int prev = (mid+n-1)%n;
            int next = (mid+1)%n;

            if(nums[mid]<nums[prev] && nums[mid]<nums[next]){
                return nums[mid];
            }
            else if(nums[mid]>nums[end]){
                start = mid+1;
            }
            else{
                end = mid -1;
            }
        }
        return -1;
    }
}
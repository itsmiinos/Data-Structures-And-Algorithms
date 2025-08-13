// Last updated: 8/13/2025, 8:21:42 PM
class Solution {
    public int findPeakElement(int[] nums) {
        int start = 0;
        int n = nums.length;
        int end = n - 1;
        int index = -1;

        if(n==1){
            return 0;
        }

        if(nums[nums.length - 1] > nums[nums.length - 2]){
return nums.length - 1;
}

        while(start<=end){
            int mid = start + (end-start)/2;
            int prev = (mid+n-1)%n;
            int next = (mid+1)%n;

            if(nums[mid]>nums[prev] && nums[mid]>nums[next]){
                return mid;
            }
            else if(nums[mid]<nums[next]){
                start = mid + 1;
            }
            else{
                end = mid -1 ;
            }
        }
        return -1;
    }
}
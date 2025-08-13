// Last updated: 8/13/2025, 8:24:10 PM
class Solution {
    public int search(int[] nums, int target) {
        int start = 0;
        int end = nums.length-1;
        int n = nums.length;
        int minimum = 0;

        while(start<=end){
            int mid = start + (end-start)/2;
            int next = (mid+1)%n;
            int prev = (mid+n-1)%n;

            if(nums[mid]<nums[prev] && nums[mid]<nums[next]){
                minimum = mid;
                System.out.println(minimum);
                break;
            }
            else if(nums[mid]>nums[end]){
                start = mid + 1;
            }
            else{
                end = mid - 1;
            }
        }

        int firstHalf = binarySearch(nums,target,0,minimum-1);
        int secondHalf = binarySearch(nums,target,minimum,nums.length-1);

        //System.out.print(minimum);

        if(firstHalf==-1){
            return secondHalf;
        }
        return firstHalf;
    
    }

    public static int binarySearch(int[] nums , int target , int start , int end){
        while(start<=end){
            int mid = start + (end-start)/2;
            if(nums[mid]==target){
                return mid;
            }
            else if(nums[mid]>target){
                end = mid - 1;
            }
            else{
                start = mid + 1;
            }
        }
        return -1;
    }
}
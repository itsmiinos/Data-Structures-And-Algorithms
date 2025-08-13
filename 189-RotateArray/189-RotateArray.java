// Last updated: 8/13/2025, 8:21:38 PM
class Solution {
    public void rotate(int[] nums, int k) {
        //7 6 5 4 3 2 1
        //5 6 7 1 2 3 4
        if(nums.length<2 || k==0 || k==nums.length){
            return;
        }
        k = k%nums.length;
        rotateHelper(nums,0,nums.length-1);
        rotateHelper(nums,0,k-1);
        rotateHelper(nums,k,nums.length-1);

    }

    public void rotateHelper(int[] nums, int i , int j){
        while(i<=j){
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
            i++;
            j--;
        }
    }
}
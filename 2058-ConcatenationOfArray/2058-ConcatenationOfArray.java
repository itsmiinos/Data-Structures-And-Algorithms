// Last updated: 8/13/2025, 8:16:51 PM
class Solution {
    public int[] getConcatenation(int[] nums) {
        int i = 0;
        int counter = 1;
        int k =0;
        int []nums_copy = new int [nums.length+nums.length]; // making a duplicate array with same elements to have a double length size.
        while(counter < 3){     //i
            counter ++;
            for(i=0;i<nums.length;i++){
                nums_copy[k] = nums[i];
                k++;
            }

            i=0;
        }

        return nums_copy;
    }
}
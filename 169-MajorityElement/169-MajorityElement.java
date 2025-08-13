// Last updated: 8/13/2025, 8:21:44 PM
class Solution {
    public int majorityElement(int[] nums) {
        int count = 0;
        int majorityElement = nums[0];

        for(int i=0;i<nums.length;i++){
            if(count==0){
                count=1;
                majorityElement = nums[i];
            }
            else if(nums[i]==majorityElement){
                count++;
            }
            else{
                count--;
            }
        }

        return majorityElement;
    }
}
// Last updated: 8/13/2025, 8:20:33 PM
class Solution {
    public int[] singleNumber(int[] nums) {
        int ans = 0;
        int n = nums.length;
        for(int i=0;i<n;i++){
            ans = ans ^ (nums[i]);
        }
        int idx = 0;
        for(int i=0;i<32;i++){
            if(checkBit(ans,i)){
                idx = i;
                break;
            }
        }
        int [] sets = new int[2];
        for(int i=0;i<n;i++){
            if(checkBit(nums[i],idx)){
                sets[0] = sets[0] ^ nums[i];
            }
            else{
                sets[1] = sets[1] ^ nums[i];
            }
        }

        return sets;
    }

    public boolean checkBit(int n , int i){
        if((n & (1<<i))==0){
            return false;
        }
        return true;
    }
}